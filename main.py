from presentation.menu import Menu
from services.mission_service import MissionService

# objects
mission_service = MissionService()   # MissionService ka object bana
menu = Menu(mission_service)         # Menu ka object bana aur MissionService ka object pass kiya
menu.display_menu()                  # Menu display karo
