from cement import Controller, ex

from core.persistence.db_models import AppUsers
from core.persistence.user_actions import delete_user, find_user_by_name
from core.utils import create_hash_password, read_master_password


class User(Controller):
    class Meta:
        label = 'user'
        stacked_type = 'nested'
        stacked_on = 'base'
        description = 'Handle user object interactions'

    @ex(help='TODO create new user',
        arguments=[
            (
                    ['-u', '--user'],
                    {
                        'help': 'select user',
                        'dest': 'username'
                    }
            )
        ])
    def create(self):
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'
        assert find_user_by_name(self.app,
                                 self.app.pargs.username) is None, 'username already exist'

        self.app.log.info('Creating user {}'.format(self.app.pargs.username))

        master_password = read_master_password(self.app)
        keys = create_hash_password(master_password, self.app.pargs.username)
        # args.vault_key = keys[0]
        master_password_hash = keys[1]
        if master_password_hash is None:
            self.app.log.fatal('Invalid master password.')
            return

        new_person = AppUsers(
            username=self.app.pargs.username,
            password_hash=master_password_hash
        )
        self.app.db.add(new_person)
        self.app.db.commit()

    @ex(help='TODO delete an user',
        arguments=[
            (
                    ['-u', '--user'],
                    {
                        'help': 'select user',
                        'dest': 'username'
                    }
            )
        ])
    def delete(self):
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        self.app.log.info('Deleting user {}'.format(self.app.pargs.username))

        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'

        keys = create_hash_password(master_password, self.app.pargs.username)
        # args.vault_key = keys[0]
        master_password_hash = keys[1]

        delete_user(self.app, self.app.pargs.username, master_password_hash)
