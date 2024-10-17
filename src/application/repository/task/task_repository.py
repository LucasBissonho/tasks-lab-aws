from abc import ABC, abstractmethod

from ....domain.task import Task


class TaskRepository(ABC):
    @abstractmethod
    async def create_task(self, t: Task):
        raise NotImplementedError

    @abstractmethod
    async def get_task_by_id(self, task_id: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    async def get_all_tasks_by_client_id(self, client_id: str) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    async def update_task(self, t: Task):
        raise NotImplementedError

    @abstractmethod
    async def delete_task(self, t: Task):
        raise NotImplementedError
