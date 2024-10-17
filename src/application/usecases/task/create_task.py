from ...repository.task.task_repository import TaskRepository
from ....domain.task import Task, StatusEnum


class CreateTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, title: str, description: str, user_id: str):
        new_task = Task(title, description, StatusEnum.TODO, user_id)
        self.task_repository.create_task(new_task)

        return new_task.to_dict()
