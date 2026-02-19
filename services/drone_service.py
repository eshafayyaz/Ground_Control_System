class DroneService:
    def update_status(self,drone,status):
        drone.drone_status = status
        return drone 