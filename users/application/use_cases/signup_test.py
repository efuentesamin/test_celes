from unittest.mock import Mock
from pydantic import ValidationError
import pytest

from users.application.schemas.user import UserCreate
from users.application.use_cases.signup import SignUpUseCase
from users.domain.entities.user import User
from users.infra.adapters.driven.sqlite_user_repository import SqliteUserRepository


repository = SqliteUserRepository()

@pytest.fixture
def user_dict():
    return {'id': 1, 'username': 'Edwin', 'password': 'pass123'}

@pytest.fixture
def save_mock(user_dict):
    user = User(user_dict['id'], user_dict['username'], user_dict['password'])
    return Mock(return_value=user)

@pytest.fixture
def repository_mock(monkeypatch, save_mock):
    monkeypatch.setattr(repository, 'create', save_mock)
    return repository

def test_signup_without_username(user_dict, repository_mock):
    with pytest.raises(ValidationError):
        use_case = SignUpUseCase(repository_mock)
        user = UserCreate(username=None, password=user_dict['password'])
        result = use_case.execute(user)

def test_signup_without_password(user_dict, repository_mock):
    with pytest.raises(ValidationError):
        use_case = SignUpUseCase(repository_mock)
        user = UserCreate(username=user_dict['username'], password=None)
        result = use_case.execute(user)

def test_signup(user_dict, repository_mock, save_mock):
    use_case = SignUpUseCase(repository_mock)
    user = UserCreate(username=user_dict['username'], password=user_dict['password'])
    result = use_case.execute(user)
    save_mock.assert_called_once()
    assert result.id == user_dict['id']
    assert result.username == user_dict['username']
    assert result.password == user_dict['password']
