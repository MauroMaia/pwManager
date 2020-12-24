from cement import Controller, ex
from cement.utils.version import get_version_banner

from core.hash_maker import generate_random_password
from ..core.version import get_version

VERSION_BANNER = """
Another password manager... %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Another password manager...'

        # text displayed at the bottom of --help output
        epilog = 'Usage: pwmanager command1 --foo bar'

        # controller level arguments. ex: 'pwmanager --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='Generate a random password',
        # sub-command level arguments. ex: 'pwmanager command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ###(['-f', '--foo'],
            ### {'help': 'notorious foo option',
            ###  'action': 'store',
            ###  'dest': 'foo'}),
        ],
    )
    def generate(self):
        """Example sub-command."""

        # data = {
        #    'foo': 'bar',
        # }

        ### do something with arguments
        # if self.app.pargs.foo is not None:
        #    data['foo'] = self.app.pargs.foo

        # self.app.render(data, 'command1.jinja2')
        new_pass = generate_random_password(self.app, 16)
        print(new_pass + "\n")