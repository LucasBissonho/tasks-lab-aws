from ....adapters.repository.repository_factory import RepositoryFactory
from ....application.usecases.user.get_user_by_username import GetUserByUsername

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    email: str
    password: str


routers = APIRouter()
routers.tags = ["Users"]


@routers.get("/user/{username}", status_code=200)
async def get_user_by_username(username: str):
    user_repo = RepositoryFactory.get_sole_instance().get_user_postgre_sole_instance()
    usecase = GetUserByUsername(user_repo)

    try:
        result = await usecase.execute(username)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return result
