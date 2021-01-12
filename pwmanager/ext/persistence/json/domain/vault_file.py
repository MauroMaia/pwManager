from typing import List

from ext.persistence.json.domain.vault_group import Group
from ext.persistence.json.domain.vault_user import User


class VaultFile(object):
    def __init__(self, user_list: List[User], group_list: List[Group]):
        #assert len(user_list) > 0, 'user_list size needs to be grater than 0'

        self.user_list = user_list
        self.group_list = group_list
