
from fastapi import HTTPException
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.application.schemas.user import User, UserCreate
from users.domain.entities.user import User as UserEntity


class SignUpUseCase:
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository
    
    def execute(self, user: UserCreate) -> User:
        db_user = self.repository.get_user_by_username(username=user.username)
        
        if db_user:
            raise HTTPException(status_code=400, detail='Username already registered')
        
        user_entity = UserEntity(None, user.username, user.password)
        user.password = user_entity.password
        return self.repository.create(user)
