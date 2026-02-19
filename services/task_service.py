class TaskHandler:
    def execute_task(self, task):

        if task.task_type == "TAKEOFF":
            print("Drone taking off")
        elif task.task_type == "MOVE":
            coords = task.parameters.get("coordinates", "0, 0")
            print(f"Drone moving to {coords}")
        elif task.task_type == "ACTION":
            action = task.parameters.get("action", "unknown")
            print(f"Drone performing action: {action}")
        elif task.task_type == "LAND":
            print("Drone landing")
        else:
            print(f"Unknown task: {task.task_type}")
