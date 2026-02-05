#FR-01: User shall be able to assign a mission to one or more drones.
from services.mission_service import MissionService
from entities.mission import Mission
from entities.drone import Drone
class Menu:
    def __init__(self, mission_service: MissionService): # Type hint: expects a MissionService object
        self.mission_service = mission_service

    def assign_mission_input(self):
        print("\n Assign Mission to Drones ")

        # Mission input
        mission_id = int(input("Enter Mission ID: "))
        mission_name = input("Enter Mission Name: ")
        description = input("Enter Mission Description: ")

        mission = Mission(mission_id, mission_name, description)

        # Drone input
        drone_count = int(input("How many drones to assign? "))
        drones = []
        for i in range(drone_count):
            print(f"\n--- Drone {i + 1} ---")
            drone_id = int(input("Enter Drone ID: "))
            model = input("Enter Drone Model: ")
            status = input("Enter Drone Status: ")
            battery_level = float(input("Enter Battery Level: "))
            location_id = int(input("Enter Location ID: "))

            drones.append(Drone(drone_id, model, status, battery_level, location_id))


    def display_menu(self):
        while True: #used while for infinite loop 
            print("\nGround Control System Menu")
            print("1. Assign Mission to Drones")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.assign_mission_input()
            elif choice == "0":
                print("Exiting")
                break
            else:
                print("Invalid choice. Please try again.")


        self.mission_service.assign_mission(mission, drones)

        print(f"\nMission '{mission.mission_name}' assigned to {len(drones)} drone(s) successfully!")
