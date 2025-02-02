📂 FastAPI DMS Backend

A lightweight, scalable Document Management System (DMS) backend built with FastAPI, SQLAlchemy, and PostgreSQL.

🚀 Features
	•	User Authentication (JWT-based)
	•	Document Upload & Retrieval
	•	Database Management with SQLAlchemy
	•	FastAPI’s interactive API documentation (Swagger and ReDoc)
	•	.env configuration for easy environment management

📁 Project Structure

dms_backend/
│── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── documents.py
│   │   │   ├── auth.py
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── __init__.py
│   ├── models/
│   │   ├── document.py
│   │   ├── user.py
│   │   ├── __init__.py
│   ├── schemas/
│   │   ├── document.py
│   │   ├── user.py
│   │   ├── __init__.py
│   ├── services/
│   │   ├── document_service.py
│   │   ├── auth_service.py
│   │   ├── __init__.py
│   ├── dependencies/
│   │   ├── database.py
│   │   ├── auth.py
│   │   ├── __init__.py
│   ├── main.py
│   ├── __init__.py
│── .env
│── requirements.txt
│── README.md
│── .gitignore

⚡️ Getting Started

1️⃣ Clone the Repository

git clone https://github.com/yourusername/dms_backend.git
cd dms_backend

2️⃣ Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root directory:

touch .env

Edit the .env file and add the variables as needed:


🛠 Running the Application

uvicorn app.main:app --reload

📌 API Endpoints

After starting the server, access the interactive API documentation:

📜 Health Check → http://127.0.0.1:8000/health