from fastapi import FastAPI

from .routes.auth.auth_user import router as auth_router
from .routes.user.create_user import routers as user_create_router
from .routes.user.get_user_by_username import routers as user_get_router
from .routes.tasks.get_all_task_by_user import routers as task_get_router
from .routes.tasks.create_task import routers as task_create_router
from .midlewares.lifespan import lifespan


app = FastAPI(title="Task List", version='1.0.0', lifespan=lifespan)


app.include_router(auth_router)
app.include_router(user_create_router)
app.include_router(user_get_router)
app.include_router(task_create_router)
app.include_router(task_get_router)
