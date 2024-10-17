from ....adapters.repository.user_repository_impl import MemoryUserRepository
from ....application.usecases.user.create_user import CreateUser

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    email: str
    password: str


routers = APIRouter()
routers.tags = ["Users"]


@routers.post("/users", status_code=201)
async def create_user(new_user: UserDTO):
    user_repo = MemoryUserRepository.get_sole_instance()
    usecase = CreateUser(user_repo)

    try:
        result = await usecase.execute(new_user.username, new_user.email, new_user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result