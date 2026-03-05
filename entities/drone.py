from pydantic import BaseModel
class Drone(BaseModel): 
    drone_id: int
    drone_name: str
    drone_status: str
        