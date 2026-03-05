from pydantic import BaseModel


class MissionCreateRequest(BaseModel):
    mission_id: int
    name: str
    description: str


class MissionCreateResponse(BaseModel):
    success: bool
    message: str


class MissionResponse(BaseModel):
    mission_id: int
    name: str
    description: str
