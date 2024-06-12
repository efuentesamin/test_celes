
from abc import ABC, abstractmethod

from users.application.schemas.user import User, UserCreate
from users.infra.models.user import User as UserModel


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, user: UserCreate) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def get_user_by_username(self, username: str) -> UserModel:
        raise NotImplementedError

