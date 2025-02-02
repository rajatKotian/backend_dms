# Allowed Origins for CORS Middleware
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "https://example.com",
]

# Temporary PDF Storage Path
TEMP_PDF_PATH = "temp.pdf"

# Extracted Output File Path
OUTPUT_TEXT_PATH = "output.txt"

# Allowed File Extensions
ALLOWED_FILE_EXTENSIONS = [".pdf"]

# Error Messages
ERROR_INVALID_FILE_FORMAT = "Invalid file format. Only PDFs are allowed."
ERROR_EMPTY_FILE = "Uploaded file is empty."
ERROR_OPENING_PDF = "Failed to open PDF file. Ensure it's a valid PDF."
ERROR_EMPTY_TEXT = "Extracted text is empty."
ERROR_PROCESSING_PDF = "Internal server error while processing PDF."
ERROR_EXTRACTING_TEXT = "Internal server error while extracting text from PDF."
ERROR_FORMATTING_TEXT = "Internal server error while formatting text."