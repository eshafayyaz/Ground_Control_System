class Drone:
        def __init__ (self, drone_id :int, drone_model :str, status :str, battery_level :float,
                       location_id :int):
            self.drone_id = drone_id
            self.drone_model = drone_model
            self.status = status
            self.battery_level = battery_level
            self.location_id = location_id