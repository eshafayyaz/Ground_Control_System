from entities import mission
from entities.drone import Drone
from entities.mission import Mission

class MissionService:
    def __init__(self):
        self.missions = []  
        
 
    def assign_mission(self, mission: Mission, drones: list[Drone]):
        mission.drones = drones 
        mission.status = "ASSIGNED"
        self.missions.append(mission) 
        return mission

 
    def get_mission_by_id(self, mission_id: int):
        for m in self.missions:
            if m.mission_id == mission_id:
                return m
        return None

 
    def start_mission(self, mission_id: int):
     mission = self.get_mission_by_id(mission_id)
     if mission:
        mission.status = "STARTED"
      
        for drone in mission.drones:
            drone.execute_mission(mission)
        return mission
     return None
    
 
    def abort_mission(self, mission_id: int):
     mission = self.get_mission_by_id(mission_id)
     if mission:
        mission.status = "ABORTED"
      
        for drone in mission.drones:
            drone.abort_mission() 
        return mission
     return None


    def complete_mission(self, mission_id: int):
     mission = self.get_mission_by_id(mission_id)
     if mission:
        mission.status = "COMPLETED"
     
        for drone in mission.drones:
            drone.complete_mission()  
        return mission
     return None

