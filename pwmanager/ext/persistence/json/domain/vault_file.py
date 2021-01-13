from datetime import datetime
from typing import List

from ext.persistence.json.domain.vault_group import Group
from ext.persistence.json.domain.vault_user import User


class VaultFile(object):
    def __init__(self, user_list: List[User], group_list: List[Group], last_update_at: datetime, created_at: datetime):
        self.user_list = user_list
        self.group_list = group_list
        self.last_update_at = last_update_at

        if created_at is not None:
            self.created_at = created_at
