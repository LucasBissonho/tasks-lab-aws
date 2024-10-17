from domain.user import User
from ...application.repository.user.user_repository import UserRepository


class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    async def create_user(self, u: User):
        self.users[u.inner_id] = u

    async def get_user_by_username(self, username: str) -> User:
        for user in self.users.values():
            if user.username == username:
                return user

        return None

    async def get_all_users(self) -> list[User]:
        return list(self.users.values())

    async def update_user(self, u: User):
        try:
            self.users[u.inner_id] = u
        except KeyError:
            print('error ao editar usuario, usuario nao encontrado')

    async def delete_user(self, u: User):
        try:
            del self.users[u.inner_id]
        except KeyError:
            print('error ao deletar usuario, usuario nao encontrado')
