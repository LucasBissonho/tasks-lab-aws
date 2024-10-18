from .....application.repository.user.user_repository import UserRepository
from ..tables.user import UserTable
from .....domain.user import User
from ..connection.postgre_connection import PostgreConnection

from sqlalchemy.future import select


class PostgreUserRepository(UserRepository):
    __sole_instance = None

    @staticmethod
    def get_sole_instance():
        if not PostgreUserRepository.__sole_instance:
            session = PostgreConnection.get_session()
            PostgreUserRepository.__sole_instance = PostgreUserRepository(
                session)
        return PostgreUserRepository.__sole_instance

    def __init__(self, session) -> None:
        if not session:
            raise ValueError('Session not provided')
        self.__session = session

    async def create_user(self, u: User):
        async with self.__session() as session:
            db_user = UserTable(
                inner_id=u.inner_id,
                username=u.username,
                password_hash=u.password_hash,
                email=u.email,
                created_at=u.created_at
            )
            session.add(db_user)

            await session.commit()

    async def get_user_by_id(self, user_id: str) -> User:
        async with self.__session() as session:
            query = select(UserTable).where(UserTable.inner_id == user_id)
            result = await session.execute(query)
            db_user = result.scalar_one_or_none()

            if not db_user:
                return None

            return User.reconstruct(
                inner_id=db_user.inner_id,
                username=db_user.username,
                password_hash=db_user.password_hash,
                email=db_user.email,
                created_at=db_user.created_at
            )

    async def get_user_by_username(self, username: str) -> User:
        async with self.__session() as session:
            query = select(UserTable).where(UserTable.username == username)
            result = await session.execute(query)
            db_user = result.scalar_one_or_none()

        if not db_user:
            return None

        return User.reconstruct(
            inner_id=db_user.inner_id,
            username=db_user.username,
            password_hash=db_user.password_hash,
            email=db_user.email,
            created_at=str(db_user.created_at)
        )

    async def get_all_users(self) -> list[User]:
        async with self.__session() as session:
            query = select(UserTable)
            result = await session.execute(query)
            db_users = result.scalars().all()

            return [User.reconstruct(
                inner_id=u.inner_id,
                username=u.username,
                password_hash=u.password_hash,
                email=u.email,
                created_at=str(u.created_at)
            ) for u in db_users]

    async def update_user(self, u: User):
        print('nao implementado')

    async def delete_user(self, u: User):
        print('nao implementado')
