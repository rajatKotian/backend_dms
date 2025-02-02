import logging

logger = logging.getLogger("fastapi_project")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)