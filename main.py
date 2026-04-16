from fastapi import FastAPI, BackgroundTasks, Depends
from sqlalchemy.orm import Session
import time

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Background job function
def process_job(job_id: int):
    db = SessionLocal()
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    
    job.status = "in_progress"
    db.commit()

    time.sleep(5)  # simulate processing

    job.status = "completed"
    job.result = "Task completed successfully"
    db.commit()

    db.close()

# Create job
@app.post("/jobs", response_model=schemas.JobResponse)
def create_job(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = models.Job()
    db.add(job)
    db.commit()
    db.refresh(job)

    background_tasks.add_task(process_job, job.id)

    return job

# Get job status
@app.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    return job