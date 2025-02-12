
from ...adapters.repository.repository_factory import RepositoryFactory
from ...application.usecases.auth.validate_user_login import ValidateUserLogin

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def validate_login(token: str = Depends(oauth2_scheme)):
    user_repo = RepositoryFactory.get_sole_instance().get_user_postgre_sole_instance()
    usecase = ValidateUserLogin(user_repo)
    try:
        result = await usecase.execute(token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result
