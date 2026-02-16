from entities import mission
from entities.mission import Mission
from entities.drone import Drone

class MissionService:
    def __init__(self):
        self.missions = []

    def assign_mission(self, mission: Mission, drones: list[Drone]):
        mission.drones = drones
        mission.status = "ASSIGNED"

        for drone in mission.drones:
            drone.status = "IDLE"
        self.missions.append(mission)
        return mission

    def start_mission(self, mission_id, task_handler=None):
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if not mission:
            print("Mission not found!")
            return False

        mission.status = "IN_PROGRESS"
        print(f"\nMission '{mission.mission_name}' is starting")

        for drone in mission.drones:
            drone.status = "IN_PROGRESS"

        executed_tasks = []

        if task_handler:
            for task in mission.tasks:
                task_handler.execute_task(task)
                executed_tasks.append(task)

        mission.status = "COMPLETED"
        for drone in mission.drones:
            drone.status = "COMPLETED"

        print("\nDrone Statuses:")
        for drone in mission.drones:
            print(f"\t Drone {drone.drone_id} named '{drone.name}' is {drone.status}.")

        print(f"\nMission '{mission.mission_name}' completed successfully!")

        return True

    def monitor_mission(self, mission_id):
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if not mission:
            print("Mission not found!")
            return False

        print(f"\n Monitoring Mission ")
        print(f"Mission Name: {mission.mission_name}")
        print(f"Mission Status: {mission.status}")
