class ReportService:
    def generate_report(self, mission):
        print("\n---------- MISSION COMPLETION REPORT ----------")
        print(f"  Mission ID    : {mission.mission_id}")
        print(f"  Mission Name  : {mission.mission_name}")
        print(f"  Description   : {mission.mission_description}")
        print(f"  Status        : {mission.status}")
        print(f"  Tasks         : {', '.join(str(t) for t in mission.tasks)}")
        print("\n  Drone Statuses:")
        for drone in mission.drones:
            print(f"\t Drone {drone.drone_id} - '{drone.drone_name}' - Status: {drone.drone_status}")
        print("-----------------------------------------------\n")


