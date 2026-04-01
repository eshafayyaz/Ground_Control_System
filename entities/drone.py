from pydantic import BaseModel
from typing import Optional, Union

class Drone(BaseModel):
    drone_id: int
    name: str
    status: str = "IDLE"
    mission: Optional[Union[dict, str]] = None  # Can be dict or string