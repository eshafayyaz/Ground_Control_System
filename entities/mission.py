from pydantic import BaseModel
from typing import List, Optional
from schemas.task_schema import Task


class Mission(BaseModel):
    mission_id: int
    name: str
    description: str
    tasks: List[Task] = []
    status: str = "created"
    assigned_drone_id: Optional[int] = None