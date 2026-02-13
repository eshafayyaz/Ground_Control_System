class TaskHandler:
    def execute_task(self, task_name): 


        if task_name == "TAKEOFF":
            print("Drone taking off")
        elif task_name == "MOVE":
            coords = input("Enter coordinates to move to (x, y, z): ")
            print(f"Drone moving to {coords}")
       
        elif task_name == "ACTION":
            action = input("Enter action to perform : ")
            print(f"Drone performing action: {action}")
        elif task_name == "LAND":
            print("Drone landing")
        else:
            print(f"Unknown task: {task_name}")