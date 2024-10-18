from sqlalchemy import Column, String, Integer, DateTime

from ..connection.postgre_connection import PostgreConnection

Base = PostgreConnection.get_base()


class TaskTable(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    inner_id = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
