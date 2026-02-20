class TaskHandler:
    def execute_task(self, task, drone_name="Drone"):

        if task.task_type == "TAKEOFF":
            print(f"{drone_name} taking off")
        elif task.task_type == "MOVE":
            coords = task.parameters.get("coordinates", "0, 0")
            print(f"{drone_name} moving to ({coords})")
        elif task.task_type == "ACTION":
            action = task.parameters.get("action", "unknown")
            print(f"{drone_name} performing action: {action}")
        elif task.task_type == "LAND":
            print(f"{drone_name} landing")
        else:
            print(f"Unknown task: {task.task_type}")
