
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.domain.entities.user import User


class SignUpUseCase:
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository
    
    def execute(self, username: str, password: str) -> User:
        if not username:
            raise(ValueError('Username is required'))

        if not password:
            raise(ValueError('Password is required'))
        
        user = User(None, username, password)
        user = self.repository.save(user)
        return user
