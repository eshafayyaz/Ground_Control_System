from typing import List
from entities.drone import Drone
from schemas.drone_schema import AssignDroneMissionResponse

class DroneService:
    def __init__(self):
        self.drones: List[Drone] = [
            Drone(drone_id=1, drone_name="Alpha", drone_status="IDLE"),
            Drone(drone_id=2, drone_name="Beta", drone_status="IDLE"),
        ]

    async def assign_mission(self, drone_id: int, mission_id: int) -> AssignDroneMissionResponse:
        drone = next((d for d in self.drones if d.drone_id == drone_id), None)
        if not drone:
            raise ValueError("Drone not found")

        drone.drone_status = f"ASSIGNED_TO_MISSION_{mission_id}"

        return AssignDroneMissionResponse(success=True, message=f"Drone {drone.drone_name} assigned to mission {mission_id}")

    async def get_all_drones(self) -> List[Drone]:
        return self.drones


drone_service = DroneService()
    