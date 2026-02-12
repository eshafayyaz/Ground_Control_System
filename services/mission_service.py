from entities import mission
from entities.drone import Drone
from entities.mission import Mission

class MissionService:
    def __init__(self):
        self.missions = []  # All assigned missions will be stored here
        
# method to assign mission to drone swarm
# we can pass objects in methods parameters --> mission is object of Mission class and drones is list of Drone objects
    def assign_mission(self, mission: Mission, drones: list[Drone]):
        mission.drones = drones # Assigned the drones for this mission
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
        # FR-03: Send commands automatically to drones
        for drone in mission.drones:
            drone.execute_mission(mission)
        return mission
     return None
    
    def abort_mission(self, mission_id: int):
     mission = self.get_mission_by_id(mission_id)
     if mission:
        mission.status = "ABORTED"
        # FR-03 logic: tell drones to stop mission
        for drone in mission.drones:
            drone.abort_mission()  # Make sure this method exists in Drone class
        return mission
     return None

    def complete_mission(self, mission_id: int):
     mission = self.get_mission_by_id(mission_id)
     if mission:
        mission.status = "COMPLETED"
        # FR-03 logic: tell drones mission is done
        for drone in mission.drones:
            drone.complete_mission()  # Make sure this method exists in Drone class
        return mission
     return None

# mission_service = MissionService() --> object od mission service call in main.py