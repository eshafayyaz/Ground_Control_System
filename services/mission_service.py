from typing import List
from entities.mission import Mission


class MissionService:
    def __init__(self):
        self.missions: List[Mission] = []

    def get_mission(self, mission_id: int) -> Mission | None:
        for mission in self.missions:
            if mission.mission_id == mission_id:
                return mission
        return None

    def get_all_missions(self) -> List[Mission]:
        return self.missions

    def create_mission(self, mission_id: int, name: str, description: str) -> None:
        existing_mission = self.get_mission(mission_id)

        if existing_mission is not None:
            raise ValueError("Mission already exists with this ID")

        new_mission = Mission(mission_id, name, description)
        self.missions.append(new_mission)
