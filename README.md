# 📂 FastAPI Document Management System (DMS) Backend

This project is a lightweight and scalable backend for a Document Management System (DMS),
built using FastAPI, SQLAlchemy, and PostgreSQL. It provides APIs for user authentication 
and document management.

# 📌 Project Structure
```
dms_backend/                         # Root directory
│── app/                             # Main application directory
│   ├── api/                         # API routes
│   │   ├── routes/                  # Route definitions
│   │   │   ├── pdf_routes.py        # PDF-related routes
│   │   │   ├── health_routes.py     # Health check route
│   │   │   ├── __init__.py          # Python package file
│   │   ├── __init__.py              # API package initializer
│   ├── services/                    # Business logic layer
│   │   ├── document_service.py      # Document service logic
│   │   ├── auth_service.py          # Authentication service logic
│   │   ├── pdf_service.py           # PDF processing logic
│   │   ├── __init__.py
│   ├── controllers/                 # API controllers (Handles request processing)
│   │   ├── document_controller.py   # Document controller logic
│   │   ├── auth_controller.py       # Authentication controller
│   │   ├── pdf_controller.py        # PDF controller logic
│   │   ├── __init__.py
│   ├── utils/                       # Utility functions
│   │   ├── logger.py                # Logger configuration
│   │   ├── constants.py             # Project-wide constants
│   │   ├── __init__.py
├── main.py                      # FastAPI entry point
├── __init__.py
│── .env                             # Environment variables (ignored in Git)
│── requirements.txt                 # Project dependencies
│── README.md                        # Project documentation
│── .gitignore                       # Ignore unnecessary files (venv, .env, __pycache__)
```

# 🚀 Getting Started

 1️⃣ Clone the Repository
```
$ git clone https://github.com/yourusername/dms_backend.git
$ cd dms_backend
```
 2️⃣ Set Up a Virtual Environment
```
$ python3 -m venv venv
$ source venv/bin/activate  # On Linux/macOS
$ venv\Scripts\activate     # On Windows
```

3️⃣ Install Dependencies
```
$ pip install -r requirements.txt
```

 4️⃣ Set Up Environment Variables
```
Create a `.env` file with and add the environment variables as needed
```
 5️⃣ Start the Application
```
Server:
$ bash start.sh

Developement:
$ bash dev.sh

```


6️⃣ Access the API Health:
```
Health : http://127.0.0.1:8000/health
```
