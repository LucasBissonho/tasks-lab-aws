from fastapi import FastAPI

from .routes.auth.auth_user import router as auth_router
from .routes.user.create_user import routers as user_create_router
from .routes.user.get_user_by_username import routers as user_get_router


app = FastAPI(title="Task List", version='1.0.0')


app.include_router(user_create_router)
app.include_router(user_get_router)
app.include_router(auth_router)
