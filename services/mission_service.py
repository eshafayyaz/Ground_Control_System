from typing import List
from entities.mission import Mission
from data_layer.db_context import DbContext
from schemas.task_schema import Task


class MissionService:
    def __init__(self, db_context: DbContext):
        self.db_context = db_context
        self.missions: List[Mission] = []

    async def create_mission(self, mission_id: int, name: str, description: str, tasks: list[Task] = None) -> Mission:
        existing_mission = await self.get_mission(mission_id)

        if existing_mission is not None:
            raise ValueError("Mission already exists with this ID")

        new_mission = Mission(mission_id, name, description, tasks)
        self.missions.append(new_mission)
        return new_mission

    async def get_mission(self, mission_id: int) -> Mission | None:
        for mission in self.missions:
            if mission.mission_id == mission_id:
                return mission
        return None

    async def get_all_missions(self) -> List[Mission]:
        return self.missions
