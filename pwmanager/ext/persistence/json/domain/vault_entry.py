import uuid

from datetime import datetime
from typing import List

from .vault_optional_attribute import OptionalAttribute


class VaultEntry(object):

    def __init__(
            self,
            username: str,
            group: str,
            encrypted_password: str,
            description: str,
            optional_attributes: List[OptionalAttribute],
            last_update_at: datetime,
            created_at: datetime,
            uid=uuid.uuid4()
    ):
        """ TODO """

#        assert username is not None, 'username should not be None'
#        assert type(username) == str, 'username type need to be string'
#        assert username != '', 'username should not be empty'

#        assert group is not None, 'group should not be None'
#        assert type(group) == str, 'group type need to be string'
#        assert group != '', 'group should not be empty'

        assert encrypted_password is not None, 'encrypted_password should not be None'
        assert type(encrypted_password) == str, 'encrypted_password type need to be str'
#        assert encrypted_password != '', 'encrypted_password should not be empty'

        self.description = description
        self.username = username
        self.group = group
        self.encrypted_password = encrypted_password
        self.custom_fields = optional_attributes
        self.last_update_at = last_update_at
        self.uid = uid

        if created_at is not None:
            self.created_at = created_at
