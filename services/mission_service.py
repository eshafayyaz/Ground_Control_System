class MissionService:
    def assign_mission(self, mission, drones):
        mission.drones = drones # Assigns drones to the mission
        mission.status = "ASSIGNED" # Sets status directly; no need to pass as parameter
        return mission

    def start_mission(self, mission):
         mission.status = "STARTED" #Just updates status; drones already assigned
         return mission

    def abort_mission(self, mission):
        mission.status = "ABORTED" # Just updates status
        return mission
    def complete_mission(self, mission):
        mission.status = "COMPLETED" # Just updates status
        return mission