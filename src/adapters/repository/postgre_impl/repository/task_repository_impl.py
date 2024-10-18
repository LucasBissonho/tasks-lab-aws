from .....application.repository.task.task_repository import TaskRepository
from ..tables.task import TaskTable
from .....domain.task import Task
from ..connection.postgre_connection import PostgreConnection

from sqlalchemy.future import select


class PostgreTaskRepository(TaskRepository):
    __sole_instance = None

    @staticmethod
    def get_sole_instance():
        if not PostgreTaskRepository.__sole_instance:
            session = PostgreConnection.get_session()
            PostgreTaskRepository.__sole_instance = PostgreTaskRepository(
                session)
        return PostgreTaskRepository.__sole_instance

    def __init__(self, session) -> None:
        self.__session = session

    async def create_task(self, t: Task):
        async with self.__session() as session:
            db_task = TaskTable(
                inner_id=t.inner_id,
                title=t.title,
                description=t.description,
                status=t.status.value,
                user_id=t.user_id,
                created_at=t.created_at
            )
            session.add(db_task)

            await session.commit()

    async def get_task_by_id(self, task_id: str) -> Task:
        async with self.__session() as session:
            query = select(TaskTable).where(TaskTable.inner_id == task_id)
            result = await session.execute(query)
            db_task = result.scalar_one_or_none()

            if not db_task:
                return None

            return Task.reconstruct(
                inner_id=db_task.inner_id,
                title=db_task.title,
                description=db_task.description,
                status=db_task.status,
                user_id=db_task.user_id,
                created_at=str(db_task.created_at)
            )

    async def get_all_tasks_by_user_id(self, client_id: str) -> list[Task]:
        async with self.__session() as session:
            query = select(TaskTable).where(TaskTable.user_id == client_id)
            result = await session.execute(query)
            db_tasks = result.scalars().all()

            return [Task.reconstruct(
                inner_id=t.inner_id,
                title=t.title,
                description=t.description,
                status=t.status,
                user_id=t.user_id,
                created_at=str(t.created_at)
            ) for t in db_tasks]

    async def update_task(self, t: Task):
        print('nao implementado')

    async def delete_task(self, t: Task):
        print('nao implementado')
