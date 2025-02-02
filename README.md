# 📂 FastAPI Document Management System (DMS) Backend

This project is a lightweight and scalable backend for a Document Management System (DMS),
built using FastAPI, SQLAlchemy, and PostgreSQL. It provides APIs for user authentication 
and document management.

# 📌 Project Structure
```
dms_backend/                         # Root directory
│── app/                              # Main application directory
│   ├── api/                          # API routes
│   │   ├── endpoints/                # Route definitions
│   │   │   ├── documents.py          # Routes for document management
│   │   │   ├── auth.py               # Routes for authentication
│   │   │   ├── __init__.py           # Python package file
│   │   ├── __init__.py               # API package initializer
│   ├── core/                         # Core configurations
│   │   ├── config.py                 # App settings
│   │   ├── database.py               # Database connection
│   │   ├── __init__.py
│   ├── models/                       # ORM Models (SQLAlchemy)
│   │   ├── document.py               # Document model
│   │   ├── user.py                   # User model
│   │   ├── __init__.py
│   ├── schemas/                      # Pydantic Schemas (Data validation)
│   │   ├── document.py               # Document schema
│   │   ├── user.py                   # User schema
│   │   ├── __init__.py
│   ├── services/                     # Business logic layer
│   │   ├── document_service.py       # Document service logic
│   │   ├── auth_service.py           # Authentication service logic
│   │   ├── __init__.py
│   ├── dependencies/                 # Dependency injection
│   │   ├── database.py               # Database session dependency
│   │   ├── auth.py                   # Authentication dependency
│   │   ├── __init__.py
│   ├── main.py                       # FastAPI entry point
│   ├── __init__.py
│── .env                              # Environment variables (ignored in Git)
│── requirements.txt                   # Project dependencies
│── README.md                         # Project documentation
│── .gitignore                        # Ignore unnecessary files (venv, .env, __pycache__)
```

# 🚀 Getting Started

 1️⃣ Clone the Repository
```
# $ git clone https://github.com/yourusername/dms_backend.git
# $ cd dms_backend
```
 2️⃣ Set Up a Virtual Environment
```
# $ python3 -m venv venv
# $ source venv/bin/activate  # On Linux/macOS
# $ venv\Scripts\activate     # On Windows
```

3️⃣ Install Dependencies
```
# $ pip install -r requirements.txt
```

 4️⃣ Set Up Environment Variables
```
# Create a `.env` file with and add the environment variables as needed
```
 5️⃣ Start the Application
```
# $ uvicorn app.main:app --reload
```

6️⃣ Access the API Health:
```
# Health : http://127.0.0.1:8000/health
```
