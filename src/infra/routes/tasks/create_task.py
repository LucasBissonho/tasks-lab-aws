from ...midlewares.validate_login import validate_login
from ....adapters.repository.repository_factory import RepositoryFactory
from ....application.usecases.task.create_task import CreateTask

from fastapi import APIRouter, Depends
from pydantic import BaseModel


routers = APIRouter()
routers.tags = ["Tasks"]


class TaskDTO(BaseModel):
    title: str
    description: str


@routers.post("/task", status_code=201)
async def create_task(new_task: TaskDTO, user_data: dict = Depends(validate_login)):
    task_repo = RepositoryFactory.get_sole_instance().get_task_postgre_sole_instance()
    usecase = CreateTask(task_repo)

    result = await usecase.execute(new_task.title, new_task.description, user_data['inner_id'])

    return result
