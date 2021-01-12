class User:
    def __init__(self, username: str, encrypted_password: str, read_only=True):
        assert username is not None, 'username should not be None'
        assert username != '', 'username should not be empty'
        assert type(username) == str, 'username type need to be string'

        assert encrypted_password is not None, 'encrypted_password should not be None'
        assert encrypted_password != '', 'encrypted_password should not be empty'
        assert type(encrypted_password) == str, 'encrypted_password type need to be string'

        self.encrypted_password = encrypted_password
        self.username = username
        self.read_only = read_only
