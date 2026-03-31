from typing import List
from entities.drone import Drone
from schemas.drone_schema import AssignDroneMissionResponse
from services.mission_service import MissionService
from data_layer.db_context import DbContext

class DroneService:
    def __init__(self, mission_service: MissionService = None):
        self.drones: List[Drone] = [
            Drone(drone_id=1, drone_name="Alpha", drone_status="IDLE"),
            Drone(drone_id=2, drone_name="Beta", drone_status="IDLE"),
        ]
        self.mission_service = mission_service

    async def assign_mission(self, drone_id: int, mission_id: int) -> AssignDroneMissionResponse:
        drone = next((d for d in self.drones if d.drone_id == drone_id), None)
        if not drone:
            raise ValueError("Drone not found")

        if self.mission_service:
            mission = await self.mission_service.get_mission(mission_id)
            if not mission:
                raise ValueError("Mission not found")

            mission.status = "assigned"
            mission.assigned_drone_id = drone_id

        drone.drone_status = f"ASSIGNED_TO_MISSION_{mission_id}"

        return AssignDroneMissionResponse(success=True, message=f"Drone {drone.drone_name} assigned to mission {mission_id}")

    async def get_all_drones(self) -> List[Drone]:
        return self.drones


# Will be initialized in main.py after mission_service is created
drone_service = None
    