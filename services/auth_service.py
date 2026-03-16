from data_layer.db_context import DbContext
from entities.user import User
from typing import Optional


class AuthService:
    def __init__(self, db_context: DbContext):
        self.db_context = db_context

    async def get_user(self, email: str) -> Optional[User]:
        for user in self.db_context.users:
            if user.email == email:
                return user
        return None

    async def login(self, email: str, password: str) -> None:
        user = await self.get_user(email)

        if user is None:
            raise ValueError("User not found with this email")

        if user.password != password:
            raise ValueError("Incorrect password")