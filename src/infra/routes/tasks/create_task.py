from ...midlewares.validate_login import validate_login
from ....adapters.repository.memory_impl.task_repository_impl import MemoryTaskRepository
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
    task_repo = MemoryTaskRepository.get_sole_instance()
    usecase = CreateTask(task_repo)

    result = await usecase.execute(new_task.title, new_task.description, user_data['inner_id'])

    return result
