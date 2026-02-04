class NotificationService:
    def send_notification(self, user, message):
        print(f"Notification sent to {user.username}: {message}")
        return f"Notification sent to {user.username}"