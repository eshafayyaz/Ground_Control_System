class Drone:
    def __init__(self, drone_id, drone_model, status, coordinates):
        self.drone_id = drone_id
        self.drone_model = drone_model
        self.status = status
        self.coordinates = coordinates
    # method to execute mission tasks
    def execute_mission(self, mission):
        print(f"\nDrone {self.drone_id} starting mission '{mission.mission_name}'...")
        for task in mission.tasks:
            print(f"Drone {self.drone_id} executing task: {task}")
        print(f"Drone {self.drone_id} completed the mission!\n")
