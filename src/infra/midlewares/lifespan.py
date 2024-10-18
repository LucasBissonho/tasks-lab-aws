from contextlib import asynccontextmanager

from ...adapters.repository.postgre_impl.connection.postgre_connection import PostgreConnection
from ...adapters.repository.repository_factory import RepositoryFactory
from ...domain.user import User

from fastapi import FastAPI

default_data = {
    "username": "lucas",
    'password_hash': '$2b$12$8d0MU0HKrZqbBh1jMo788OpEJXd1lL2KEoB6LwHa712aRqJIEGuRm',
    "email": "lucas@email.com",
    "created_at": "2024-10-17 01:48:48.380178+00:00",
    "inner_id": "cda02b03-4eae-4bc2-b706-dcf519eac5a8"
}
default_user = User.reconstruct(**default_data)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # starting the application
    await PostgreConnection.init_database()
    repo = RepositoryFactory.get_sole_instance().get_user_postgre_sole_instance()
    is_user = await repo.get_user_by_username('lucas')
    if is_user is None:
        repo.create_user(default_user)
    yield
    # Clean up for shutdown the application
