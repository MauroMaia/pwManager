from cement import Controller, ex

from core.utils import read_master_password, create_hash_password


class Vault(Controller):
    class Meta:
        label = 'vault'
        stacked_type = 'nested'
        stacked_on = 'base'

    @ex(help='TODO list vaults')
    def list(self):
        pass

    @ex(help='Create new vault',
        arguments=[
            (
                    ['-u', '--user'],
                    {
                        'help': 'select user',
                        'dest': 'username'
                    }
            ),
            (
                    ['-n', '--name'],
                    {
                        'help': 'Give a name to the vault',
                        'dest': 'username'
                    }
            )
        ])
    def create(self):
        assert self.app.pargs.username is not None, 'username should be defined'
        assert self.app.pargs.username != '', 'username should be different form empty string'

        master_password = read_master_password(self.app)
        keys = create_hash_password(master_password, self.app.pargs.username)
        # args.vault_key = keys[0]
        master_password_hash = keys[1]

        assert master_password is not None, 'Invalid master password.'

        # assert find_user_by_name_and_hash(self.app,
        #                                  self.app.pargs.username,
        #                                  master_password) is not None, 'username does not exist'

        pass

    @ex(help='TODO update an existing vault')
    def update(self):
        pass

    @ex(help='TODO delete an vault')
    def delete(self):
        pass

    @ex(help='TODO delete an vault')
    def entry(self):
        pass
