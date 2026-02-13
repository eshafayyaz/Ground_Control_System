from entities.mission import Mission
from entities.drone import Drone
class MissionService:
    def __init__ (self):
        self.missions=[]
          
    def assign_mission(self,mission: Mission, drones: list[Drone]):
        mission.drones= drones
        mission.status = "ASSIGNED"
        self.missions.append(mission)
        return mission 
    def start_mission(self, mission_id, task_handler=None):
        mission= next((m for m in self.missions if m.mission_id == mission_id), None)
    
        if not mission:
            return False

        mission.status = "IN_PROGRESS"
        print(f"\nMission '{mission.mission_name}' is starting")

        if task_handler:
            for task in mission.tasks:
                print(f"\n Executing task: {task} ") 
                task_handler.execute_task(task)

        mission.status = "COMPLETED"
        print(f"\nMission '{mission.mission_name}' completed successfully!")
        return True
   
