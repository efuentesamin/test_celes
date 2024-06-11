
from shared_kernel.database import SessionLocal
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.application.schemas.user import User, UserCreate
from users.infra import models


class SqliteUserRepository(UserRepositoryInterface):

    def __init__(self) -> None:
        super().__init__()
        self.db = SessionLocal()

    def create(self, user: UserCreate) -> User:
        db_user = models.User(username=user.username, hashed_password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(*db_user)
