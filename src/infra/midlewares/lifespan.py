from contextlib import asynccontextmanager

from ...adapters.repository.postgre_impl.connection.postgre_connection import PostgreConnection
from ...adapters.repository.postgre_impl.connection.create_default_user import create_default_user

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # starting the application
    await PostgreConnection.init_database()
    await create_default_user()
    yield
    # Clean up for shutdown the application
