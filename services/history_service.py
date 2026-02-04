class HistoryService:
    def log_action(self, history):
     # Shows what action the user did and when on the screen
     print(f"User {history.user_id} did '{history.action}' at {history.timestamp}") 
     return history
