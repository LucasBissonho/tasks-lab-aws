from abc import ABC
import uuid


class Entity(ABC):
    __slots__ = ("__inner_id",)

    def __init__(self, inner_id: str = None):
        self.__inner_id = self.__create_inner_id(inner_id)

    def __create_inner_id(self, id: str = None) -> uuid.UUID:
        if id:
            is_valid_id = self.is_valid_inner_id(id)

            if not is_valid_id:
                raise ValueError("Invalid UUID")

            return uuid.UUID(id)
        else:
            return uuid.uuid4()

    @property
    def inner_id(self) -> str:
        return str(self.__inner_id)

    @staticmethod
    def is_valid_inner_id(inner_id: str) -> bool:
        try:
            uuid.UUID(inner_id)
            return True
        except ValueError:
            return False
