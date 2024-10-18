from enum import Enum
from datetime import datetime

from .entity import Entity


class StatusEnum(str, Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class Task(Entity):
    __slots__ = ('__title', '__description', '__status',
                 '__user_id', '__created_at')

    def __init__(self, title: str, description: str, status: StatusEnum, user_id: str, inner_id: str = None):
        super().__init__(inner_id)

        self.set_title(title)
        self.set_description(description)
        self.set_status(status)
        self.set_user_id(user_id)
        self.__created_at = datetime.now()

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def status(self) -> StatusEnum:
        return self.__status

    @property
    def user_id(self) -> str:
        return self.__user_id

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def set_title(self, title: str):
        self.__title = title

    def set_description(self, description: str):
        self.__description = description

    def set_status(self, status: StatusEnum):
        self.__status = status

    def set_user_id(self, user_id: str):
        self.__user_id = user_id

    def to_dict(self) -> dict:
        return {
            'inner_id': self.inner_id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def reconstruct(cls, inner_id: str, title: str, description: str, status: str, user_id: str, created_at: str):
        task = cls(title, description, StatusEnum(status), user_id, inner_id)
        task.__created_at = datetime.fromisoformat(created_at)

        return task
