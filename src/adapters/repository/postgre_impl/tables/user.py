from sqlalchemy import Column, String, Integer, DateTime

from ..connection.postgre_connection import PostgreConnection

Base = PostgreConnection.get_base()


class UserTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    inner_id = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
