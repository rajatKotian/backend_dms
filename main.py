from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.pdf_routes import pdf_router
from app.routes.health_routes import health_router
from app.utils.constants import ALLOWED_ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(pdf_router)