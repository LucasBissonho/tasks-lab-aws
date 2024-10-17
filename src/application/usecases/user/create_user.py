from ...repository.user.user_repository import UserRepository
from ....domain.user import User


class CreateUser:
    def __init__(self, user_repo: UserRepository) -> dict:
        self.user_repo = user_repo

    async def execute(self, username: str, email: str, password: str):
        is_user = await self.user_repo.get_user_by_username(username)
        if is_user:
            raise ValueError(f"User with username {username} already exists")

        new_user = User(username, email, password)

        await self.user_repo.create_user(new_user)

        return new_user.to_dict()
