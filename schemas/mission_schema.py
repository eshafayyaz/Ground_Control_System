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

class AssignMissionRequest(BaseModel):
    mission_id: int
    drone_id: str
 
class AssignMissionResponse(BaseModel):
    success: bool
    message: str
    drone_id: str
    mission_id: int
    mission_name: str
class StartMissionRequest(BaseModel):
    mission_id: int

class StartMissionResponse(BaseModel):
    success: bool
    message: str
    mission_id: int
    mission_name: str
    status: str
    tasks_count: int