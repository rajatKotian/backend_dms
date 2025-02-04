from fastapi import FastAPI,HTTPException
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from app.routes.pdf_routes import pdf_router
from app.routes.health_routes import health_router
from app.utils.constants import ERROR_RATE_LIMITER

load_dotenv()


app = FastAPI()

limiter = Limiter(key_func=get_remote_address, default_limits=["100/second"]) 
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request, exc: RateLimitExceeded):
    return HTTPException(
        status_code=400, 
        detail=ERROR_RATE_LIMITER
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_HOSTS", "").split(","),  # Read from .env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Added Limiter for all the routes
app.add_middleware(SlowAPIMiddleware)

app.include_router(health_router)
app.include_router(pdf_router)