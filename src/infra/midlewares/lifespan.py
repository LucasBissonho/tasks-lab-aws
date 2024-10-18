from contextlib import asynccontextmanager

from ...adapters.repository.postgre_impl.connection.postgre_connection import PostgreConnection

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # starting the application
    await PostgreConnection.init_database()
    yield
    # Clean up for shutdown the application
