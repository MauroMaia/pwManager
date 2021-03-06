from cement import Controller, ex

from ..core.utils import create_hash_password, read_master_password, check_for_password_exploits


class User(Controller):
    class Meta:
        label = 'user'
        stacked_type = 'nested'
        stacked_on = 'base'
        description = 'Feature is still work in progress.(Multi-tenant/Shared Vaults)'

    @ex(help='Create new user',
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
        assert self.app.db.find_user_by_name(self.app.pargs.username) is None, 'username already exist'

        self.app.log.info('Creating user {}'.format(self.app.pargs.username))

        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'
        assert check_for_password_exploits(self.app, master_password) is not True, 'Insecure password for this feature'

        keys = create_hash_password(master_password, self.app.pargs.username)
        # args.vault_key = keys[0]
        master_password_hash = keys[1]
        if master_password_hash is None:
            self.app.log.fatal('Invalid master password.')
            return

        self.app.db.add_new_db_user(self.app.pargs.username,master_password_hash)

    #@ex(help='TODO delete an user',
    #    arguments=[
    #        (
    #                ['-u', '--user'],
    #                {
    #                   'help': 'select user',
    #                    'dest': 'username'
    #                }
    #        )
    #    ])
    def delete(self):
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        self.app.log.info('Deleting user {}'.format(self.app.pargs.username))

        master_password = read_master_password(self.app)
        assert master_password is not None, 'Invalid master password.'

        keys = create_hash_password(master_password, self.app.pargs.username)
        # args.vault_key = keys[0]
        master_password_hash = keys[1]

        #delete_user(self.app, self.app.pargs.username, master_password_hash)
