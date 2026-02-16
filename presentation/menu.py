from entities.mission import Mission
from entities.drone import Drone
from services.mission_service import MissionService
from services.task_service import TaskHandler

class Menu:
    def __init__(self, mission_service: MissionService):
        self.mission_service = mission_service
        self.task_handler = TaskHandler()

    def assign_mission_input(self):
        print("\n Assign a mission to drone swarm")
        mission_id = int(input("Enter Mission ID: "))
        mission_name = input("Enter Mission Name: ")
        mission_description = input("Enter Mission Description: ")

        tasks = ["TAKEOFF", "MOVE", "ACTION", "LAND"]

        mission = Mission(
            mission_id,
            mission_name,
            mission_description,
            tasks, 
        )

        print("\nMission created successfully!")
        print("Tasks assigned:")
        for t in tasks:
            print(f"- {t}")

        drone_swarm = [
            Drone(
                drone_id=1,
                drone_model="Swarm of Drones",
                name="Swarm Alpha",
                status="available",
                coordinates=(0.0, 0.0)
            )

        ]

        self.mission_service.assign_mission(mission, drone_swarm)
        print(f"\nMission '{mission.mission_name}' assigned to drone swarm successfully!")

    def start_mission_input(self):
        print("\nStart a Mission")
        mission_id = int(input("Enter Mission ID to start: "))

        success = self.mission_service.start_mission(mission_id, self.task_handler)
        if not success:
            print(f"\nMission {mission_id} not found or cannot be started.")

    def show_main_menu(self):
        while True:
            print("\nGround Control System Menu")
            print("1. Assign Mission to Drone Swarm")
            print("2. Start Mission / Execute Tasks")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.assign_mission_input()
            elif choice == "2":
                self.start_mission_input()
            elif choice == "3":
                print("Exiting Ground Control System Goodbye!")
                break   
            else:
                print("Invalid choice. Try again.")
