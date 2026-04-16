# Background Job Processing System (FastAPI)

## 📌 Project Description
This project is a backend service built using FastAPI that handles asynchronous job processing. Users can create jobs and track their status until completion.

---

## 🚀 Features
- Create background jobs
- Track job status (pending, in_progress, completed)
- Asynchronous processing using FastAPI BackgroundTasks
- SQLite database integration
- Swagger API documentation

---

## ⚙️ Setup Instructions

```bash
pip install -r requirements.txt
uvicorn main:app --reload