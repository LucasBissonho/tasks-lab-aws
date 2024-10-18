import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import dotenv

dotenv.load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


class PostgreConnection:
    __session = None
    __engine = None
    __base = None

    @staticmethod
    def get_session():
        if PostgreConnection.__session is None:
            engine = PostgreConnection.get_engine()
            PostgreConnection.__session = sessionmaker(
                engine, class_=AsyncSession, expire_on_commit=False)

        return PostgreConnection.__session

    @staticmethod
    def get_engine():
        if PostgreConnection.__engine is None:
            PostgreConnection.__engine = create_async_engine(
                DATABASE_URL, echo=True)

        return PostgreConnection.__engine

    @staticmethod
    def get_base():
        if PostgreConnection.__base is None:
            PostgreConnection.__base = declarative_base()

        return PostgreConnection.__base

    @staticmethod
    async def create_tables():
        base = PostgreConnection.get_base()
        engine = PostgreConnection.get_engine()

        async with engine.begin() as conn:
            await conn.run_sync(base.metadata.create_all)

    @staticmethod
    async def init_database():
        engine = PostgreConnection.get_engine()
        base = PostgreConnection.get_base()

        async with engine.begin() as conn:
            await conn.run_sync(base.metadata.create_all)
