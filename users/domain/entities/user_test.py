import pytest

from users.domain.entities.user import User


@pytest.fixture
def new_user():
    return {'id': 1, 'username': 'Edwin', 'password': 'pass123'}

def test_create_user_without_username(new_user):
    with pytest.raises(ValueError) as execinfo:
        user = User(None, None, new_user['password'])

    assert str(execinfo.value) == 'Username is required'

def test_create_user_without_password(new_user):
    with pytest.raises(ValueError) as execinfo:
        user = User(None, new_user['username'], None)

    assert str(execinfo.value) == 'Password is required'

def test_create_user(new_user):
    user = User(new_user['id'], new_user['username'], new_user['password'])
    assert user.id == new_user['id']
    assert user.username == new_user['username']
    assert user.password == new_user['password']
