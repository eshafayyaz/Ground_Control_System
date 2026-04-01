from typing import List
import httpx
from entities.drone import Drone
from schemas.drone_schema import AssignDroneMissionResponse
from services.mission_service import MissionService
from data_layer.db_context import DbContext
from config import DRONE_API_BASE_URL, DRONE_API_TIMEOUT

class DroneService:
    def __init__(self, mission_service: MissionService = None):
        self.mission_service = mission_service
        self.http_client = httpx.AsyncClient(
            base_url=DRONE_API_BASE_URL,
            timeout=DRONE_API_TIMEOUT
        )

    async def assign_mission(self, drone_id: int, mission_id: int) -> AssignDroneMissionResponse:
        # Get mission details from mission service
        if not self.mission_service:
            raise ValueError("Mission service not initialized")

        mission = await self.mission_service.get_mission(mission_id)
        if not mission:
            raise ValueError("Mission not found")

        try:
            # Call external drone API with query parameters
            response = await self.http_client.post(
                f"/assign-mission/{drone_id}",
                params={
                    "mission_id": mission.mission_id,
                    "name": mission.name,
                    "description": mission.description
                }
            )
            response.raise_for_status()

            # Update mission status in our system
            mission.status = "assigned"
            mission.assigned_drone_id = drone_id

            # Get drone name from external API response
            result = response.json()
            drone_name = result.get("drone_name", f"Drone {drone_id}")

            # Create detailed message
            message = f"Mission '{mission.name}' assigned to drone '{drone_name}'"

            return AssignDroneMissionResponse(
                success=True,
                message=message
            )

        except httpx.HTTPStatusError as e:
            raise ValueError(f"Failed to assign mission: {e.response.text}")
        except httpx.RequestError as e:
            raise ValueError(f"Connection error to drone API: {str(e)}")

    async def get_all_drones(self) -> List[Drone]:
        
        try:
            response = await self.http_client.get("/drones")
            response.raise_for_status()

            drones_data = response.json()
            return [Drone(**drone) for drone in drones_data]

        except httpx.HTTPStatusError as e:
            raise ValueError(f"Failed to fetch drones: {e.response.text}")
        except httpx.RequestError as e:
            raise ValueError(f"Connection error to drone API: {str(e)}")

    async def close(self):
        """Close HTTP client connection"""
        await self.http_client.aclose()

drone_service = None
    