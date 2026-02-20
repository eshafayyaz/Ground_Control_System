from entities.mission import Mission
from entities.drone import Drone
from services.command_service import CommandService
from services.drone_service import DroneService
from services.task_service import TaskHandler

class MissionService:
    def __init__(self):
        self.missions = []
        self.command_service = CommandService()
        self.drone_service = DroneService()
        self.task_handler = TaskHandler()

    def assign_mission(self, mission: Mission, drone: list[Drone]):
        mission.drones = drone
        mission.status = "ASSIGNED"

        for drone in mission.drones:
            self.drone_service.update_status(drone, "IDLE")
            print(f"{drone.drone_name} status: {drone.drone_status}")
        self.missions.append(mission)
        return mission

    def start_mission(self, mission_id):
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if not mission:
            print("Mission not found!")
            return False

        if mission.status != "ASSIGNED":
            print(f"Mission '{mission.mission_name}' is '{mission.status}'. Cannot start.")
            return False

        mission.status = "IN_PROGRESS"
        print(f"\nMission '{mission.mission_name}' is starting")

        for drone in mission.drones:
            self.drone_service.update_status(drone, "IN_PROGRESS")
            print(f"{drone.drone_name} status: {drone.drone_status}")
            self.command_service.send_commands(drone, mission)
            self.execute_mission(drone, mission)

        mission.status = "COMPLETED"
        for drone in mission.drones:
            self.drone_service.update_status(drone, "COMPLETED")
            print(f"{drone.drone_name} status: {drone.drone_status}")

        return True

    def execute_mission(self, drone, mission):
        print(f"\n{drone.drone_name} starting mission '{mission.mission_name}'...")
        for task in mission.tasks:
            self.task_handler.execute_task(task, drone.drone_name)
        print(f"{drone.drone_name} completed the mission!\n")

    def abort_mission(self, mission_id): 
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if not mission:
            print("Mission not found!")
            return False

        if mission.status not in ("ASSIGNED", "IN_PROGRESS"):
            print(f"Mission '{mission.mission_name}' is '{mission.status}'. Cannot abort.")
            return False

        mission.status = "ABORTED"
        for drone in mission.drones:
            self.drone_service.update_status(drone, "IDLE")
            print(f"{drone.drone_name} status: {drone.drone_status}")

        return True
