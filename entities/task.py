class Task:
    def __init__(self, task_type, parameters=None):
        self.task_type = task_type
        self.parameters = parameters or {}

    def __str__(self):
        if self.task_type == "MOVE":
            return f"MOVE to ({self.parameters.get('coordinates', '')})"
        elif self.task_type == "ACTION":
            return f"ACTION - {self.parameters.get('action', '')}"
        return self.task_type