from services.task_service import TaskHandler
class CommandService:
    def __init__(self):
        self.task_handler = TaskHandler()

    def update_commands(self, command, name, parameters):
        command.command_name = name
        command.parameters = parameters
        return command

    def send_commands(self, drone, mission):
        print(f"\nSending commands to {drone.drone_name}")
