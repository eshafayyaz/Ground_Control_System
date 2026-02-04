class command:
    def __init__ (self, command_id :int, command_name :str, parameters :str):
        self.command_id = command_id
        self.command_name = command_name
        self.parameters = parameters