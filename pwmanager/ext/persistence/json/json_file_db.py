import os
import pickle
import zlib
from datetime import datetime

from ext.persistence.VaultDatabaseInterface import VaultDatabaseInterface
from ext.persistence.json.domain.vault_entry import VaultEntry
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
                entries=list(),
                created_at=datetime.now(),
                last_update_at=datetime.now()
            )

    def load_data(self) -> bool:
        """Overrides InformalParserInterface.load_data_source()"""
        file = open(self.path, "rb")

        data_compressed = file.read()
        data_decompressed = zlib.decompress(data_compressed)
        vf = pickle.loads(data_decompressed)

        file.close()

        self.vault = vf
        return True

    def save_data(self) -> bool:
        """Overrides VaultDatabaseInterface.save_data()"""

        # set file last modification time
        self.vault.last_update_at = datetime.now()

        # TODO encrypt the file content

        # save to file
        file = open(self.path, "wb")

        str_dump = pickle.dumps(self.vault)
        str_compressed = zlib.compress(str_dump)
        file.write(str_compressed)

        file.close()
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

        self.vault.user_list.append(User(username, master_password_hash, datetime.now(), datetime.now()))
        self.save_data()

    def add_new_entry(self, entry: VaultEntry):
        assert entry is not None, 'entry should not be None'

        self.vault.entries.append(entry)
        pass

    def find_entry_by_description(self, entry_description):
        assert entry_description is not None, 'entry_description should not be None'
        assert entry_description != '', 'entry_description should not be empty'
        assert type(entry_description) == str, 'entry_description type need to be string'

        for entry in self.vault.entries:
            if entry.description == entry_description:
                return entry

        for group in self.vault.group_list:
            for entry in group.entries:
                if entry.description == entry_description:
                    return entry

        return None

    def find_all_entry_by_description(self, entry_description):
        assert entry_description is not None, 'entry_description should not be None'
        assert entry_description != '', 'entry_description should not be empty'
        assert type(entry_description) == str, 'entry_description type need to be string'

        result = []

        for entry in self.vault.entries:
            if entry_description in entry.description:
                result.append(entry)

        for group in self.vault.group_list:
            for entry in group.entries:
                if entry_description in entry.description:
                    result.append(entry)

        return result

    def find_all_entry_by_uuid(self, entry_uuid):
        assert entry_uuid is not None, 'entry_uuid should not be None'
        assert entry_uuid != '', 'entry_uuid should not be empty'
        assert type(entry_uuid) == str, 'entry_uuid type need to be string'

        result = []

        for entry in self.vault.entries:
            if entry_uuid in entry.description:
                result.append(entry)

        for group in self.vault.group_list:
            for entry in group.entries:
                if entry_uuid in entry.description:
                    result.append(entry)

        return result
