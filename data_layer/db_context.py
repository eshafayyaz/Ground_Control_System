from entities.user import User

class DbContext:
    users: list[User] = [
        User(id=1, email="hy@example.com", password="password123"),
        User(id=2, email="hi@example.com", password="secret456"),
    ]
