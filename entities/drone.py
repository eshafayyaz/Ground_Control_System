class Drone: 
    def __init__(self, drone_id, drone_name, drone_status):
        self.drone_id = drone_id  
        self.drone_status = drone_status  
        self.drone_name = drone_name  
        
    def execute_mission(self, mission):
        print(f"\nDrone {self.drone_id} starting mission '{mission.mission_name}'...")
        for task in mission.tasks:
            print(f"Drone {self.drone_id} executing task: {task}")
        print(f"Drone {self.drone_id} completed the mission!\n")