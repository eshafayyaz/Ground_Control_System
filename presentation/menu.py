from entities.mission import Mission
from entities.task import Task
from entities.drone import Drone


class Menu:
    def __init__(self, mission_service):
        self.mission_service = mission_service

    def assign_mission_input(self):
        print("\n Assign a mission to drone swarm")
        mission_id = int(input("Enter Mission ID: "))
        mission_name = input("Enter Mission Name: ")
        mission_description = input("Enter Mission Description: ")

        print("\nTasks Assigning:")
        tasks = []
        tasks.append(Task("TAKEOFF"))

       
        print("TAKEOFF")

        move_count = 0
        while True:
            coords= input("Enter MOVE coordinates (x,y) or 'done': ")
            if coords.lower() == "done":
                break
            move_count += 1
            tasks.append(Task("MOVE", {"coordinates": coords}))
            print(f"MOVE Point {move_count} ({coords})")

        action_count = 0
        while True:
            action = input("Enter ACTION or 'done': ")
            if action.lower() == "done":
                break
            action_count += 1
            tasks.append(Task("ACTION", {"action": action}))
            print(f"Action {action_count}: {action}")

        tasks.append(Task("LAND"))
        print("LAND")

        mission = Mission(
            mission_id,
            mission_name,
            mission_description,
            tasks,
        )

        drone_swarm = [
            Drone(
                drone_id=1,
                drone_name="Swarm Alpha",
                drone_status="available"
            )

        ]

        self.mission_service.assign_mission(mission, drone_swarm)
        print(f"\nMission '{mission.mission_name}' assigned to drone swarm successfully!")


    def start_mission_input(self):
        print("\nStart a Mission")
        mission_id = int(input("Enter Mission ID to start: "))

        success = self.mission_service.start_mission(mission_id)
        if not success:
            print(f"\nMission {mission_id} not found or cannot be started.")

    def abort_mission_input(self):
        print("\nAbort a Mission")
        mission_id = int(input("Enter Mission ID to abort: "))

        success = self.mission_service.abort_mission(mission_id)
        if not success:
            print(f"\nMission {mission_id} could not be aborted.")

    def show_main_menu(self):
        while True:
            print("\nGround Control System Menu")
            print("1. Assign Mission to Drone Swarm")
            print("2. Start Mission / Execute Tasks")
            print("3. Abort Mission")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.assign_mission_input()
            elif choice == "2":
                self.start_mission_input()
            elif choice == "3":
                self.abort_mission_input()
            elif choice == "4":
                print("Exiting Ground Control System Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
