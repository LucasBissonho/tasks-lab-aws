from .routes.user.create_user import routers as user_create_router
from .routes.user.get_user_by_username import routers as user_get_router

from fastapi import FastAPI

app = FastAPI(title="Task List", version='1.0.0')


app.include_router(user_create_router)
app.include_router(user_get_router)
