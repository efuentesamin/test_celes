
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.application.schemas.user import User, UserCreate
from users.domain.entities.user import User as UserEntity


class SignUpUseCase:
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository
    
    def execute(self, user: UserCreate) -> User:
        user_entity = UserEntity(None, user.username, user.password)
        user_dto = UserCreate(username=user_entity.username, password=user_entity.password)
        return self.repository.create(user_dto)
