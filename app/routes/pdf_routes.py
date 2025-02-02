from fastapi import APIRouter, UploadFile, File
from app.controllers.pdf_controller import process_pdf

pdf_router = APIRouter()

@pdf_router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    return await process_pdf(file)