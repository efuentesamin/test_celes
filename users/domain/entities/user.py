import bcrypt

class User:
    def __init__(self, id: int, username: str, password: str):
        if not username:
            raise(ValueError('Username is required'))

        if not password:
            raise(ValueError('Password is required'))

        self.id = id
        self.username = username

        # If this instance has no id (it's new) the password needs to be hashed
        if not self.id:
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            password = hash.decode('utf-8')
        
        self.password = password
