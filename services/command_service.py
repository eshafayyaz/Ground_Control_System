class CommandService:
    def send_commands(self, drone: 'Drone', mission: 'Mission'):
        print(f"\nSending commands to {drone.drone_name}")