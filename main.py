from presentation.menu import Menu
from services.mission_service import MissionService

# objects
mission_service = MissionService()  
menu = Menu(mission_service)         
menu.display_menu()                 
