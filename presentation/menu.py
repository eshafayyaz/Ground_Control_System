# Import Relevant Entities and Services 

from entities.mission import Mission
from entities.drone import Drone 
from services.mission_service import MissionService

#Menu class: handles user input and actions
class Menu:
    def __init__(self, mission_service:MissionService):
        self.mission_service= mission_service

# ------ FR-01: User shall be able to assign a mission to one or more drones.------#
#  
    # This method will handle the input for assigning a mission to drones
    def assign_mission_input(self):
        print("\n Assign a mission to drones")

        # Mission input
    
        mission_id = int(input("Enter Mission_ID: "))
        mission_name = input("Enter Mission_Name: ")
        mission_description = input("Enter Mission_Description: ")
        mission = Mission(mission_id,mission_name,mission_description) #Mission() --> Mission object created here

        # Drone Input 

        drone_count = int(input("How many drones to assign : "))

    #we will store multiple drones in this list

        drones = []
        for i in range (drone_count):
          print(f"\n Drone {i+1}")
        drone_id = int(input("Enter Drone_ID :"))
        drone_model = input("Enter Drone_Model :")
        status = input(" Enter Drone Status (available/busy):")
        battery_level = float(input("Enter Battery_Level:"))
        location_id = int(input("Enter Location_ID: "))

        # Create and save drone object in list

        drones.append(Drone(drone_id, drone_model, status, battery_level,location_id))
        #Call the service to assign the mission to the drones
        self.mission_service.assign_mission(mission, drones)

        print(f"\n Mission '{mission.mission_name}' assigned to {len(drones)} drone(s) successfully!")
     
    # This method will display the menu and handle user input

     # ------- FR-02: Start Mission -------- #

    def start_mission_input(self):
        print("\n Start a Mission")
        mission_id = int(input("Enter Mission_ID to start: "))

        # Call service to start mission
        success = self.mission_service.start_mission(mission_id)
        if success:
            print(f"\n Mission {mission_id} started successfully!")
        else:
            print(f"\n Mission {mission_id} not found or cannot be started.")

    def display_menu(self):
        while True: # Infinite loop to keep the menu running until user chooses to exit
            print("\n Ground_Control_System")
            print("1. Assign a mission")
            print("2. Start a Mission")
            print("0. Exit")
          
            choice = int(input("Enter your choice:"))
            if choice == 1:
             self.assign_mission_input() # if choice 1 call assign_mission_input() 
            elif choice == 2:
                self.start_mission_input()# if choice 2 call start_mission_input() 
            elif choice == 0:
             print("Exiting")
             break
        else:
          print("Invalid choice. Please try again.")
