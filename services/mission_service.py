from entities.drone import Drone
from entities.mission import Mission

class MissionService:
    def __init__(self):
        self.missions = []  # All assigned missions will be stored here

    def assign_mission(self, mission: Mission, drones: list[Drone]):
        mission.drones = drones
        mission.status = "ASSIGNED"
        self.missions.append(mission)  # Save mission in list
        return mission

    # Find mission by ID
    def get_mission_by_id(self, mission_id: int):
        for m in self.missions:
            if m.mission_id == mission_id:
                return m
        return None

    # Start mission using mission object
    def start_mission(self, mission_id: int):
        mission = self.get_mission_by_id(mission_id)
        if mission:
            mission.status = "STARTED"
            return mission
        else:
            return None

    def abort_mission(self, mission_id: int):
        mission = self.get_mission_by_id(mission_id)
        if mission:
            mission.status = "ABORTED"
            return mission
        return None

    def complete_mission(self, mission_id: int):
        mission = self.get_mission_by_id(mission_id)
        if mission:
            mission.status = "COMPLETED"
            return mission
        return None

# mission_service = MissionService() --> object od mission service call in main.py