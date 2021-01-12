from typing import List

from ext.persistence.json.domain.vault_optional_attribute import OptionalAttribute


class VaultEntry(object):

    def __init__(self, username: str, encrypted_password: str, description: str,
                 optional_attributes: List[OptionalAttribute]):
        assert username is not None, 'username should not be None'
        assert username != '', 'username should not be empty'
        assert type(username) == str, 'username type need to be string'

        assert encrypted_password is not None, 'encrypted_password should not be None'
        assert encrypted_password != '', 'encrypted_password should not be empty'
        assert type(encrypted_password) == str, 'encrypted_password type need to be string'

        self.description = description
        self.username = username
        self.encrypted_password = encrypted_password
        self.custom_fields = optional_attributes
