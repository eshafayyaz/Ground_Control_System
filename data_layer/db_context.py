from entities.user import User

class DbContext:
    users: list[User] = [
        User(id=1, email="esha@example.com", password="esha123"),
        User(id=2, email="maryam@example.com", password="maryam123"),
    ]

    