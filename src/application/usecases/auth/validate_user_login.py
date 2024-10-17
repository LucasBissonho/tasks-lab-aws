from ...repository.user.user_repository import UserRepository


class ValidateUserLogin:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, token: str) -> dict:
        user = await self.user_repository.get_user_by_id(token)
        if not user:
            raise ValueError("Invalid token")

        return user.to_dict()
