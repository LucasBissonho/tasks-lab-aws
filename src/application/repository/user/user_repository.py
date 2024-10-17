from abc import ABC, abstractmethod

from ....domain.user import User


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, u: User):
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> User:
        raise NotImplementedError

    # @abstractmethod
    # async def get_user_by_email(self, email: str) -> User:
    #     raise NotImplementedError

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    async def update_user(self, u: User):
        raise NotImplementedError

    @abstractmethod
    async def delete_user(self, u: User):
        raise NotImplementedError
