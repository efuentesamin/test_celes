
from abc import ABC, abstractmethod

from users.domain.entities.user import User


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

