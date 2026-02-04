class CommandService:
     def update_commands (self,command,name,parameters):
          command.command_name= name
          command.parameters= parameters
          return command
     def send_commands (self, drone, mission):
          for command in mission.command :# we will give here multiple commands so we used for loop 
               drone.execute(command)
     