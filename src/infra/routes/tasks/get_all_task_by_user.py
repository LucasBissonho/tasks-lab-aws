from ...midlewares.validate_login import validate_login
from ....adapters.repository.task_repository_impl import MemoryTaskRepository
from ....application.usecases.task.get_tasks_by_user import GetTasksByUserId

from fastapi import APIRouter, Depends
from pydantic import BaseModel


routers = APIRouter()
routers.tags = ["Tasks"]


class TaskDTO(BaseModel):
    title: str
    description: str


@routers.get("/task", status_code=200)
async def get_all_tasks_by_user(user_data: dict = Depends(validate_login)):
    task_repo = MemoryTaskRepository.get_sole_instance()
    usecase = GetTasksByUserId(task_repo)

    result = await usecase.execute(user_data['inner_id'])

    return result
