from datetime import datetime, timezone

from passlib.context import CryptContext

from .entity import Entity


class User(Entity):
    __slots__ = ('__username', '__password_hash', '__email', '__created_at')

    def __init__(self, username: str, email: str, password: str = None, inner_id: str = None):
        super().__init__(inner_id)
        self.__username = username
        self.__email = email
        if password:
            self.__password_hash = self.__create_password_hash(password)
        self.__created_at = datetime.now(timezone.utc)

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password_hash(self) -> str:
        return self.__password_hash if not None else None

    @property
    def email(self) -> str:
        return self.__email

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def verify_password(self, password: str) -> bool:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(password, self.__password_hash)

    def __create_password_hash(self, password: str) -> str:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)

    def set_password_hash(self, password_hash: str):
        self.__password_hash = password_hash

    def set_created_at(self, created_at: datetime):
        self.__created_at = created_at

    def to_dict(self) -> dict:
        return {
            "username": self.__username,
            "email": self.__email,
            "created_at": str(self.__created_at),
            "inner_id": self.inner_id
        }

    @classmethod
    def reconstruct(cls, username: str, password_hash: str, email: str, created_at: str, inner_id: str):
        user = cls(username, email, inner_id=inner_id)
        user.set_password_hash(password_hash)
        user.set_created_at(datetime.fromisoformat(created_at))

        return user
