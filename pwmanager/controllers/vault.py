from cement import Controller, ex


class Vault(Controller):
    class Meta:
        label = 'vault'
        stacked_type = 'nested'
        stacked_on = 'base'

    @ex(help='TODO list vaults')
    def list(self):
        pass

    @ex(help='TODO create new vault')
    def create(self):
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
