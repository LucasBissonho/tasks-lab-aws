from ...application.repository.task.task_repository import TaskRepository
from ...domain.task import Task


class MemoryTaskRepository(TaskRepository):
    __sole_instance = None

    def __init__(self):
        self.tasks = {}

    @staticmethod
    def get_sole_instance():
        if MemoryTaskRepository.__sole_instance is None:
            MemoryTaskRepository.__sole_instance = MemoryTaskRepository()
        return MemoryTaskRepository.__sole_instance

    async def create_task(self, t: Task):
        self.tasks[t.inner_id] = t

    async def get_task_by_id(self, task_id: str) -> Task:
        return self.tasks.get(task_id)

    async def get_all_tasks_by_user_id(self, client_id: str) -> list[Task]:
        return [task for task in self.tasks.values() if task.client_id == client_id]

    async def update_task(self, t: Task):
        try:
            self.tasks[t.inner_id] = t
        except KeyError:
            print('error ao editar task, task nao encontrado')

    async def delete_task(self, t: Task):
        try:
            del self.tasks[t.inner_id]
        except KeyError:
            print('error ao deletar task, task nao encontrado')
