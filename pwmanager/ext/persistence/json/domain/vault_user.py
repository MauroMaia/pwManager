from datetime import datetime


class User:
    def __init__(
            self,
            username: str,
            password_hash: str,
            last_update_at: datetime,
            created_at: datetime,
            read_only=True
    ):
        """ TODO """

        assert username is not None, 'username should not be None'
        assert username != '', 'username should not be empty'
        assert type(username) == str, 'username type need to be string'

        assert password_hash is not None, 'password_hash should not be None'
        assert password_hash != '', 'password_hash should not be empty'
        assert type(password_hash) == str, 'password_hash type need to be string'

        self.password_hash = password_hash
        self.username = username
        self.read_only = read_only
        self.last_update_at = last_update_at

        if created_at is not None:
            self.created_at = created_at
