from pydantic import BaseModel

class JobCreate(BaseModel):
    task_name: str

class JobResponse(BaseModel):
    id: int
    status: str
    result: str | None

    class Config:
        orm_mode = True