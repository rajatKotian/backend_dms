import fitz
import os
import re
from fastapi import HTTPException
from app.utils.logger import logger
from app.utils.constants import (
    TEMP_PDF_PATH, OUTPUT_TEXT_PATH,
    ERROR_EMPTY_FILE, ERROR_OPENING_PDF,
    ERROR_EMPTY_TEXT, ERROR_EXTRACTING_TEXT, ERROR_FORMATTING_TEXT
)

async def extract_text_from_pdf(file):
    """
    Extracts and processes text from an uploaded PDF file.
    Args:
        file (UploadFile): The uploaded PDF file.
    Returns:
        str: The structured text extracted from the PDF.
    Raises:
        HTTPException: Raises 400 for client errors (invalid file, empty file, or corrupt PDF).
        HTTPException: Raises 500 for unexpected server errors during processing.
    """
    try:

        pdf_data = file.file.read()

        if not pdf_data:
            raise HTTPException(status_code=400, detail=ERROR_EMPTY_FILE)
        

        with open(TEMP_PDF_PATH, "wb") as f:
            f.write(pdf_data)

        try:
            doc = fitz.open(TEMP_PDF_PATH)
        except Exception:
            raise HTTPException(status_code=400, detail=ERROR_OPENING_PDF)


        extracted_text = "\n".join([page.get_text() for page in doc])


        structured_text = format_text(extracted_text)


        with open(OUTPUT_TEXT_PATH, "w", encoding="utf-8") as f:
            f.write(structured_text)


        os.remove(TEMP_PDF_PATH)

        return structured_text

    except HTTPException as e:

        logger.error(f"Client error: {str(e.detail)}")
        raise
    
    except Exception as e:

        logger.error(f"Unexpected error extracting text from PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=ERROR_EXTRACTING_TEXT)
    

def format_text(text):
    """
    Formats extracted text into a hierarchical structured format based on indentation rules.
    Args:
        text (str): The raw extracted text from the PDF.
    Returns:
        str: The formatted text with proper indentation.
    Raises:
        HTTPException: Raises 400 if the extracted text is empty.
        HTTPException: Raises 500 for unexpected errors during text formatting.
    """
    try:
        
        if not text.strip():
            raise HTTPException(status_code=400, detail=ERROR_EMPTY_TEXT)

        lines = text.split("\n")
        structured_text = []
        indent = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if re.match(r"^\d+\..*", line):  
                indent = 0
            elif re.match(r"^\d+\.\d+.*", line):  
                indent = 1
            elif re.match(r"^\d+\.\d+\.\d+.*", line):  
                indent = 2
            else:
                indent = min(indent + 1, 3)  

            structured_text.append("\t" * indent + line)

        return "\n".join(structured_text)

    except HTTPException as e:
        logger.error(f"Client error: {str(e.detail)}")
        raise
    
    except Exception as e:
        logger.error(f"Unexpected error formatting text: {str(e)}")
        raise HTTPException(status_code=500, detail=ERROR_FORMATTING_TEXT)
    finally:
        if os.path.exists(TEMP_PDF_PATH):
            os.remove(TEMP_PDF_PATH)