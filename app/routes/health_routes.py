from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
def health():
    return {"status": True, "message": "System is up and running"}