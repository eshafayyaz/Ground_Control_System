from schemas.task_schema import Task


class Mission:
    def __init__(self, mission_id: int, name: str, description: str, tasks: list[Task] = None):
        self.mission_id = mission_id
        self.name = name
        self.description = description
        self.tasks = tasks if tasks is not None else []
        self.status = "created"  # created, assigned, in_progress, completed
        self.assigned_drone_id = None

    def to_dict(self):
        """Convert mission to dict format for external API"""
        return {
            "id": self.mission_id,
            "name": self.name,
            "description": self.description
        }