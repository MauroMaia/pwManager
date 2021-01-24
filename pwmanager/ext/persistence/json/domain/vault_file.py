from datetime import datetime
from typing import List

from ext.persistence.json.domain.vault_entry import VaultEntry
from ext.persistence.json.domain.vault_user import User


class VaultFile(object):
    def __init__(
            self,
            user_list: List[User],
            entries: List[VaultEntry],
            last_update_at: datetime,
            created_at: datetime
    ):
        """ TODO """

        self.user_list = user_list
        self.entries = entries
        self.last_update_at = last_update_at

        if created_at is not None:
            self.created_at = created_at
