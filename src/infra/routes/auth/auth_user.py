from ....adapters.repository.user_repository_impl import MemoryUserRepository
from ....application.usecases.auth.auth_user import AuthenticateUser


from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter()
router.tags = ["Authentication"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user_repository = MemoryUserRepository.get_sole_instance()
    auth_user = AuthenticateUser(data_repo=user_repository)

    try:
        result = await auth_user.perform(form_data.username, form_data.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return result
