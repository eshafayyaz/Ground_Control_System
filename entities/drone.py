from pydantic import BaseModel
from typing import Optional, Union, Dict, Any

class Drone(BaseModel):
    drone_id: int
    name: str
    status: str = "IDLE"
    mission: Optional[Union[Dict[str, Any], str]] = None  # Can be dict or string