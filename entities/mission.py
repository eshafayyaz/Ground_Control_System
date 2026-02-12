class Mission:
    def __init__(self, mission_id, mission_name, mission_description, tasks):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.tasks = tasks
        self.drones = []  # Drones assigned to this mission
        self.status = "PENDING"  # Initial status of the mission
