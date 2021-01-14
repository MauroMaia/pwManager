import uuid
from datetime import datetime
from typing import List

from ext.persistence.json.domain.vault_entry import VaultEntry
from ext.persistence.json.domain.vault_optional_attribute import OptionalAttribute


class Group(object):
    def __init__(
            self,
            name: str,
            optional_attributes: List[OptionalAttribute],
            entries: List[VaultEntry],
            last_update_at: datetime,
            created_at: datetime,
            uid=uuid.uuid4()
    ):
        """ TODO """

        self.name = name
        self.optional_attributes = optional_attributes
        self.entries = entries
        # self.sub_groups = sub_groups
        self.last_update_at = last_update_at
        self.uid = uid

        if created_at is not None:
            self.created_at = created_at
