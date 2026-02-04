class sensor_data:
    def __init__ (self, data_id :int, sensor_type :str, value :float, timestamp :str):
        self.data_id = data_id
        self.sensor_type = sensor_type
        self.value = value
        self.timestamp = timestamp