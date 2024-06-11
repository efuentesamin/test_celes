
from abc import ABC, abstractmethod

from users.application.schemas.user import User, UserCreate


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, user: UserCreate) -> User:
        raise NotImplementedError

