from .memory_impl.user_repository_impl import MemoryUserRepository
from .memory_impl.task_repository_impl import MemoryTaskRepository
from .postgre_impl.repository.user_repository_impl import PostgreUserRepository
from .postgre_impl.repository.task_repository_impl import PostgreTaskRepository


class RepositoryFactory:
    __sole_instance = None

    @staticmethod
    def get_sole_instance():
        if not RepositoryFactory.__sole_instance:
            RepositoryFactory.__sole_instance = RepositoryFactory()
        return RepositoryFactory.__sole_instance

    def get_user_memory_sole_instance(self) -> MemoryUserRepository:
        return MemoryUserRepository.get_sole_instance()

    def get_task_memory_sole_instance(self) -> MemoryTaskRepository:
        return MemoryTaskRepository.get_sole_instance()

    def get_user_postgre_sole_instance(self) -> PostgreUserRepository:
        return PostgreUserRepository.get_sole_instance()

    def get_task_postgre_sole_instance(self) -> PostgreTaskRepository:
        return PostgreTaskRepository.get_sole_instance()
