from fastapi import UploadFile, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.utils.logger import logger
from app.utils.constants import ERROR_INVALID_FILE_FORMAT, ALLOWED_FILE_EXTENSIONS

async def process_pdf(file: UploadFile):
    """
    Processes an uploaded PDF file by extracting and formatting its text.
    Args:
        file (UploadFile): The uploaded PDF file.
    Returns:
        dict: A JSON response containing the structured text output.
    Raises:
        HTTPException: 400 if the file format is invalid.
        HTTPException: 500 if there is an internal server error during processing.
    """
    try:
        if not any(file.filename.endswith(ext) for ext in ALLOWED_FILE_EXTENSIONS):
            raise HTTPException(status_code=400, detail=ERROR_INVALID_FILE_FORMAT)
        
        structured_text = await extract_text_from_pdf(file)
        return {"message": "Text extracted and structured successfully", "output": structured_text}
    
    except HTTPException as e:
        logger.error(f"Client error: {str(e.detail)}")
        raise
    
    except Exception as e:
        logger.error(f"Server error processing PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error while processing PDF.")