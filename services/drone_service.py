class DroneService:
    def update_status(self,drone,status):
        drone.status= status
        return drone 
    def update_battery(self, drone, battery_level):
        drone.battery_level = battery_level
        return drone # Return the updated drone object so it can be used later