from services.task_service import TaskHandler

class CommandService:
    def __init__(self):
        self.task_handler = TaskHandler()

    def update_commands(self, command, name, parameters):
        command.command_name = name
        command.parameters = parameters
        return command

    def send_commands(self, drone, mission):  
        print(f"\nSending commands to Drone {drone.drone_id} ('{drone.drone_name}')")
        for task in mission.tasks:
            self.task_handler.execute_task(task)
 