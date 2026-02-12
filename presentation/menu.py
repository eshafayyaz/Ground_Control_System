# Import Relevant Entities and Services
from entities.mission import Mission
from entities.drone import Drone
from services.mission_service import MissionService


# Menu class: handles user input and actions
class Menu:
    def __init__(self, mission_service: MissionService):
        self.mission_service = mission_service

    # ------ FR-01: Assign Mission to Drone Swarm ------ #
    
    # This method will handle the input for assigning a mission to drone swarm
    def assign_mission_input(self):
        print("\n Assign a mission to drone swarm")

        # Mission basic info input
        mission_id = int(input("Enter Mission ID: "))
        mission_name = input("Enter Mission Name: ")
        mission_description = input("Enter Mission Description: ")  

        # Mission tasks input
        tasks = []
        print("\n Enter mission tasks (type 'done' when finished):")
        while True:
            task = input("Enter task: ")
            if task.lower() == "done":
                break
            tasks.append(task)

        # Create Mission object with tasks
        mission = Mission(
            mission_id,
            mission_name,
            mission_description,
            tasks,  # tasks list included
        )

        print("\nMission created successfully!")
        print("Tasks assigned: ")
        # for loop to display tasks assigned to the mission
        for t in tasks:
            print(f"- {t}")

        # create drone swarm object 
        drone_swarm = [
            Drone(
                drone_id=1,
                drone_model="Swarm of Drones",
                status="available",
                coordinates=(0.0, 0.0)
            )
        ]


        # Assign mission to drone swarm
        # using the assign_mission method of mission service to assign the created mission to the drone swarm
        self.mission_service.assign_mission(mission, drone_swarm)

        print(f"\n Mission '{mission.mission_name}' assigned to drone swarm successfully!")

    # ------- FR-02: Start Mission -------- #
    # This method will handle the input for starting a mission

    def start_mission_input(self):
        print("\n Start a Mission")

        mission_id = int(input("Enter Mission ID to start: "))

        success = self.mission_service.start_mission(mission_id)

        if success:
            print(f"\nMission {mission_id} started successfully!")
        else:
            print(f"\nMission {mission_id} not found or cannot be started.")

    #this method will display the menu and handle user choices

    def display_menu(self):
        while True:
            print("\n Ground Control System Menu")
            print("1. Assign Mission to Drone Swarm")
            print("2. Start Mission")
            print("3. Exit")

            choice = input("\n Enter your choice: ")

            if choice == "1":
                self.assign_mission_input()
            elif choice == "2":
                self.start_mission_input()
            elif choice == "3":
                print("Exiting Ground Control System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")