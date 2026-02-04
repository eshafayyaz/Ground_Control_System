class LocationService:
    def update_location(self, location, latitude, longitude):
        location.latitude = latitude
        location.longitude = longitude
        return location
