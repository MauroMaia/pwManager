import json
from datetime import datetime

from cement import Controller, ex

from core.crypto import generate_random_password, encrypt, decrypt
from core.utils import read_master_password, create_hash_password, json_default
from ext.persistence.json.domain.vault_entry import VaultEntry


class Entry(Controller):
    class Meta:
        label = 'entry'
        stacked_type = 'nested'
        stacked_on = 'vault'

    @ex(help='TODO create new user',
        arguments=[
            # TODO - ACL by username/password
            (
                    # FIXME - split username of owner/accessUser from entry username
                    ['-u', '--user'],
                    {
                        'help': 'User password user name',
                        'dest': 'username'
                    }
            ),
            (
                    ['-d', '--description'],
                    {
                        'help': 'Name to give to the new entry.',
                        'dest': 'entry_description'
                    }
            ),
            (
                    ['-p', '--password'],
                    {
                        'help': 'Password that should be stored. If not present, will be generated one.',
                        'dest': 'password',
                    }
            )
        ])
    def create(self):
        # Basic pargs validations
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        assert self.app.pargs.entry_description is not None, 'entry_description should be defined'
        assert self.app.pargs.entry_description != '', 'entry_description should be different form empty string'

        # check if user exist
        user = self.app.db.find_user_by_name(self.app.pargs.username)
        if user is None:
            self.app.log.fatal("User %s does not exit in database".format(self.app.pargs.username))
            return

        # get hash user password
        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'

        keys = create_hash_password(master_password, self.app.pargs.username)
        vault_key = keys[0]
        master_password_hash = keys[1]

        # check if password is valid
        if master_password_hash is None or user.password_hash != master_password_hash:
            self.app.log.fatal('Invalid master password.')
            return

        # TODO - Check if entry exist
        entry = self.app.db.find_entry_by_description(self.app.pargs.entry_description)
        assert entry is None, 'Invalid entry description. Description "%s" already exist.'.format(
            self.app.pargs.entry_description)

        # if is a new entry

        # TODO - generate a new random password
        if self.app.pargs.password == '':
            self.app.log.fatal('Invalid password.')
            return

        if self.app.pargs.password is None:
            self.app.pargs.password = generate_random_password(self.app, 16)

        encrypted_password = encrypt(self.app.pargs.password, vault_key)

        entry = VaultEntry(
            self.app.pargs.username,
            encrypted_password.decode(),
            self.app.pargs.entry_description,
            optional_attributes=[],
            last_update_at=datetime.now(),
            created_at=datetime.now()
        )

        self.app.db.add_new_entry(entry)
        self.app.db.save_data()

        # TODO - show information to the user
        print("Raw password: " + self.app.pargs.password
              + "\nAdded new entry:\n" + json.dumps(
            entry.__dict__,
            ensure_ascii=False,
            default=json_default,
            indent=4
        ))

    @ex(help='TODO create new user',
        arguments=[
            (
                    ['-u', '--user'],
                    {
                        'help': 'User password user name',
                        'dest': 'username'
                    }
            ),
            (
                    ['-d', '--description'],
                    {
                        'help': 'Name search for.',
                        'dest': 'entry_description'
                    }
            ),
        ])
    def list(self):
        # Basic pargs validations
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        assert self.app.pargs.entry_description is not None, 'entry_description should be defined'
        assert self.app.pargs.entry_description != '', 'entry_description should be different form empty string'

        # check if user exist
        user = self.app.db.find_user_by_name(self.app.pargs.username)
        if user is None:
            self.app.log.fatal("User %s does not exit in database".format(self.app.pargs.username))
            return

        # get hash user password
        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'

        keys = create_hash_password(master_password, self.app.pargs.username)
        vault_key = keys[0]
        master_password_hash = keys[1]

        # check if password is valid
        if master_password_hash is None or user.password_hash != master_password_hash:
            self.app.log.fatal('Invalid master password.')
            return

        # TODO - Check if entry exist
        entry = self.app.db.find_all_entry_by_description(self.app.pargs.entry_description)

        print(json.dumps(
            entry,
            ensure_ascii=False,
            default=json_default,
            sort_keys=True,
            indent=4
        ))

    @ex(help='TODO create new user',
        arguments=[
            (
                    ['-u', '--user'],
                    {
                        'help': 'User password user name',
                        'dest': 'username'
                    }
            ),
            (
                    ['-d', '--description'],
                    {
                        'help': 'Name search for.',
                        'dest': 'entry_description'
                    }
            ),
            (
                    ['-i', '--uuid'],
                    {
                        'help': 'UUID to search for.',
                        'dest': 'entry_UUID'
                    }
            ),
        ])
    def decrypt(self):
        # Basic pargs validations
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        if self.app.pargs.entry_description is None \
                and self.app.pargs.entry_UUID is None:
            assert True, 'entry_description or entry_UUID must be defined'
        if self.app.pargs.entry_description is None:
            assert self.app.pargs.entry_UUID != '', 'entry_UUID must not be empty'

        if self.app.pargs.entry_UUID is None:
            assert self.app.pargs.entry_description != '', 'entry_description must not be empty'

        # check if user exist
        user = self.app.db.find_user_by_name(self.app.pargs.username)
        if user is None:
            self.app.log.fatal("User %s does not exit in database".format(self.app.pargs.username))
            return

        # get hash user password
        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'

        keys = create_hash_password(master_password, self.app.pargs.username)

        vault_key = keys[0]
        master_password_hash = keys[1]

        # check if password is valid
        if master_password_hash is None or user.password_hash != master_password_hash:
            self.app.log.fatal('Invalid master password.')
            return

        entries = []

        if self.app.pargs.entry_description is None:
            entries = self.app.db.find_all_entry_by_description(self.app.pargs.entry_description)

        if self.app.pargs.entry_UUID is None:
            entries = self.app.db.find_all_entry_by_description(self.app.pargs.entry_description)

        for entry in entries:
            print(
                "{} - {}".format(
                    entry.username,
                    decrypt(
                        entry.encrypted_password,
                        vault_key
                    ).decode()
                )
            )
