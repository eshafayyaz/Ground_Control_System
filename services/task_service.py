from schemas.task_schema import TakeoffTask, MoveTask, ActionTask, LandTask

class TaskHandler:
    async def execute_task(self, task, drone_name: str = "Drone"):
        if isinstance(task, TakeoffTask):
            print(f"{drone_name} taking off")
        elif isinstance(task, MoveTask):
            print(f"{drone_name} moving to ({task.coordinates})")
        elif isinstance(task, ActionTask):
            print(f"{drone_name} performing action: {task.action}")
        elif isinstance(task, LandTask):
            print(f"{drone_name} landing")