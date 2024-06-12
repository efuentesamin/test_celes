
import bcrypt
from fastapi import HTTPException
from shared_kernel.auth_handler import sign_jwt
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.application.schemas.user import UserCreate


class LoginUseCase:
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository
    
    def execute(self, user: UserCreate):
        db_user = self.repository.get_user_by_username(username=user.username)
        
        if not db_user:
            raise ValueError('Invalid credentials')
        
        password_bytes = user.password.encode('utf-8')
        hash = db_user.hashed_password.encode('utf-8')
        match = bcrypt.checkpw(password_bytes, hash)

        if not match:
            raise ValueError('Invalid credentials')
        
        return sign_jwt(user.username)
