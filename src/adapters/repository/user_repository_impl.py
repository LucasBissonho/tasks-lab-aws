from ...domain.user import User
from ...application.repository.user.user_repository import UserRepository


class MemoryUserRepository(UserRepository):
    default_user = {
        "username": "lucas",
        'password_hash': '$2b$12$8d0MU0HKrZqbBh1jMo788OpEJXd1lL2KEoB6LwHa712aRqJIEGuRm',
        "email": "lucas@email.com",
        "created_at": "2024-10-17 01:48:48.380178+00:00",
        "inner_id": "cda02b03-4eae-4bc2-b706-dcf519eac5a8"
    }
    __sole_instance = None

    def __init__(self):
        self.users = {}

    # def __new__(cls):
    #     if cls.__sole_instance is None:
    #         cls.__sole_instance = super(MemoryUserRepository, cls).__new__(cls)
    #     return cls.__sole_instance
    @staticmethod
    def get_sole_instance():
        if MemoryUserRepository.__sole_instance is None:
            MemoryUserRepository.__sole_instance = MemoryUserRepository()
            user = User.reconstruct(**MemoryUserRepository.default_user)
            MemoryUserRepository.__sole_instance.users[user.inner_id] = user
        return MemoryUserRepository.__sole_instance

    async def create_user(self, u: User):
        self.users[u.inner_id] = u

    async def get_user_by_username(self, username: str) -> User:
        for user in self.users.values():
            if user.username == username:
                return user

        return None

    async def get_user_by_id(self, user_id: str) -> User:
        return self.users.get(user_id)

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
