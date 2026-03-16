from pydantic import BaseModel


class Task(BaseModel):
    task_type: str
    parameters: dict = {}
