class Mission:
    def __init__(self, mission_id: int, mission_name: str, description: str, commands=None):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.description = description
        self.commands = commands if commands else []  # yahi commands ki list hai
