from ....domain.task import Task
from ...repository.task.task_repository import TaskRepository


class GetTasksByUserId:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def execute(self, user_id: str) -> list[Task]:
        tasks = await self.task_repository.get_all_tasks_by_user_id(user_id)

        return [task.to_dict() for task in tasks]
