
from shared_kernel.database import SessionLocal
from users.application.ports.driven.user_repository import UserRepositoryInterface
from users.application.schemas.user import User, UserCreate
from users.infra.models.user import User as UserModel


class SqliteUserRepository(UserRepositoryInterface):

    def __init__(self) -> None:
        super().__init__()
        self.db = SessionLocal()

    def create(self, user: UserCreate) -> User:
        db_user = UserModel(username=user.username, hashed_password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(
            id=db_user.id,
            username=db_user.username,
        )

    def get_user_by_username(self, username: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.username == username).first()

