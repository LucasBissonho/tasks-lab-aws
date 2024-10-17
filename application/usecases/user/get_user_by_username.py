from ...repository.user.user_repository import UserRepository


class GetUserByUsername:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, username: str) -> dict:
        user = await self.user_repository.get_user_by_username(username)

        if not user:
            raise ValueError(f"User with username {username} not found")

        return user.to_dict()
