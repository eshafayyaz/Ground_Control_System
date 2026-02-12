class HistoryService:
    def log_action(self, history):
     print(f"User {history.user_id} did '{history.action}' at {history.timestamp}") 
     return history
