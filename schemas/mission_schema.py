from pydantic import BaseModel
from schemas.task_schema import Task


class MissionCreateRequest(BaseModel):
    mission_id: int
    name: str
    description: str
    tasks: list[Task] = []


class MissionCreateResponse(BaseModel):
    success: bool
    message: str


class MissionResponse(BaseModel):
    mission_id: int
    name: str
    description: str
    tasks: list[Task] = []
