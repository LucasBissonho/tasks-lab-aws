from .memory_impl.user_repository_impl import MemoryUserRepository
from .memory_impl.task_repository_impl import MemoryTaskRepository


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
