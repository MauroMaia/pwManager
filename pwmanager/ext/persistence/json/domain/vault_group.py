from typing import List

from ext.persistence.json.domain.vault_entry import VaultEntry
from ext.persistence.json.domain.vault_optional_attribute import OptionalAttribute


class Group(object):
    def __init__(self, name,
                 optional_attributes: List[OptionalAttribute],
                 enties: List[VaultEntry]):
        self.name = name
        self.optional_attributes = optional_attributes
        self.enties = enties
        # self.sub_groups = sub_groups
