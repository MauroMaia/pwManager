from cement import Controller, ex
from cement.utils.version import get_version_banner

from ..core.crypto import generate_random_password
from ..core.utils import check_for_password_exploits
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
        # epilog = 'Usage: pwmanager <command> --foo bar'
        epilog = "This project was created for an academic purpose. So the content on this project, of which Mauro " \
                 "Filipe Maia <dev@maurofilipemaia.dev> is the author, is licensed under MIT license (" \
                 "https://opensource.org/licenses/MIT).\n\n" \
                 "Copyright 2021 Mauro Filipe Maia\n\n" \
                 "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and " \
                 "associated documentation files (the \"Software\"), to deal in the Software without restriction, " \
                 "including without limitation the rights to use, copy, modify, merge, publish, distribute, " \
                 "sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is " \
                 "furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this " \
                 "permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE " \
                 "SOFTWARE IS PROVIDED \"AS  IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT " \
                 "NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND " \
                 "NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, " \
                 "DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, " \
                 "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."

        # controller level arguments. ex: 'pwmanager --version'
        arguments = [
            ### add a version banner
            (
                ['-v', '--version'],
                {
                    'action': 'version',
                    'version': VERSION_BANNER
                }
            ),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='Generate a random password',
        # sub-command level arguments. ex: 'pwmanager command1 --foo bar'
        arguments=[
            (['-s', '--size'], {
                'help': 'Password size',
                'action': 'store',
                'dest': 'size',
                'type': int,
                'default': 16
            })
        ],
    )
    def generate(self):
        """Example sub-command."""
        password = generate_random_password(self.app, self.app.pargs.size)
        check_for_password_exploits(self.app, password)
        print(password + "\n")
