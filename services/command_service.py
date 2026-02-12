class CommandService:
     def update_commands (self,command,name,parameters):
          command.command_name= name
          command.parameters= parameters
          return command
     def send_commands (self, drone, mission):
          for command in mission.command :
               drone.execute(command)
     