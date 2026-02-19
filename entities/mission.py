class Mission:
    def __init__(self, mission_id, mission_name, mission_description, tasks):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.tasks = tasks
        self.drones = []
        self.status = "PENDING"

