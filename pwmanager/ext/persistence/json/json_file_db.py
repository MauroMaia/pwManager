import os
import pickle
from datetime import datetime

from ext.persistence.VaultDatabaseInterface import VaultDatabaseInterface
from ext.persistence.json.domain.vault_file import VaultFile
from ext.persistence.json.domain.vault_user import User


class JsonFileDB(VaultDatabaseInterface):

    def __init__(self, path: str):
        assert path is not None, 'path should not be None'
        assert path != '', 'path should not be empty'
        assert type(path) == str, 'path type need to be string'

        self.path = path
        self.vault = None

        if os.path.exists(self.path):
            self.load_data()
        else:
            self.vault = VaultFile(
                user_list=list(),
                group_list=list(),
                created_at=datetime.now(),
                last_update_at=datetime.now()
            )

    def load_data(self) -> bool:
        """Overrides InformalParserInterface.load_data_source()"""
        f = open(self.path, "rb")
        vf = pickle.load(f)
        f.close()

        self.vault = vf
        return True

    def save_data(self) -> bool:
        """Overrides VaultDatabaseInterface.save_data()"""

        # set file last modification time
        self.vault.last_update_at = datetime.now()

        # save to file
        f = open(self.path, "wb")
        pickle.dump(self.vault, f)
        f.close()

        # TODO encrypt the file

        return True

    def find_user_by_name(self, username=None):
        assert username is not None, 'username should not be None'
        assert username != '', 'username should not be empty'
        assert type(username) == str, 'username type need to be string'

        assert self.vault is not None, 'vault should not be None'

        for user in self.vault.user_list:
            if user.username == username:
                return user

        return None

    def find_group_by_name(self, group_name=None):
        assert group_name is not None, 'group_name should not be None'
        assert group_name != '', 'group_name should not be empty'
        assert type(group_name) == str, 'group_name type need to be string'

        # Fixme this is not the this should be done. group_name can (and will be) a path.
        group_list = []
        for group in self.vault.group_list:
            if group.name == group_name:
                group_list.append(group)
            # group_list.append(find_group_by_name(group, group_name))
        return group_list

    def add_new_db_user(self, username, master_password_hash):
        assert username is not None, 'username should not be None'
        assert username != '', 'username should not be empty'
        assert type(username) == str, 'username type need to be string'

        assert master_password_hash is not None, 'master_password_hash should not be None'
        assert master_password_hash != '', 'master_password_hash should not be empty'
        assert type(master_password_hash) == str, 'master_password_hash type need to be string'

        self.vault.user_list.append(User(username, master_password_hash))
        self.save_data()
