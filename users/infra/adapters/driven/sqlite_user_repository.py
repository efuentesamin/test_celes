
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.domain.entities.user import User


class SqliteUserRepository(UserRepositoryInterface):

    def save(self, user: User) -> User:
        pass
