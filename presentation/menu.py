class Menu:
    def show_menu(self):
        print("\n--- Ground Control System Menu ---")
        print("1. Assign Mission to Drones")
        print("2. Start Mission (Send Commands Automatically)")
        print("0. Exit")

        choice = input("Enter your choice: ")
        return choice
