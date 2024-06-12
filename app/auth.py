from fastapi import APIRouter, HTTPException

from users.application.schemas.user import User, UserCreate
from users.application.use_cases.login import LoginUseCase
from users.application.use_cases.signup import SignUpUseCase
from users.infra.adapters.driven.sqlite_user_repository import SqliteUserRepository

router = APIRouter()


@router.post('/signup', response_model=User)
def create_user(user: UserCreate):
    try:
        repository = SqliteUserRepository()
        use_case = SignUpUseCase(repository)
        return use_case.execute(user)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post('/login')
def user_login(user: UserCreate):
    try:
        repository = SqliteUserRepository()
        use_case = LoginUseCase(repository)
        return use_case.execute(user)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
