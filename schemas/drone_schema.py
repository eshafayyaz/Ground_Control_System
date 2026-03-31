from pydantic import BaseModel
from typing import List
from entities.drone import Drone

class AssignDroneMissionRequest(BaseModel):
    drone_id: int
    mission_id: int

class AssignDroneMissionResponse(BaseModel):
    success: bool
    message: str

class DroneListResponse(BaseModel):
    drones: List[Drone]
