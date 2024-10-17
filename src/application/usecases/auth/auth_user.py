from ...repository.user.user_repository import UserRepository


class AuthenticateUser:
    def __init__(self, data_repo: UserRepository):
        self.data_repo = data_repo

    async def perform(self, username: str, password: str) -> dict:
        user = await self.data_repo.get_user_by_username(username)

        if not user or not user.verify_password(password):
            raise ValueError("Invalid username or password")

        return {
            **user.to_dict(),
            'access_token': user.inner_id,
        }
