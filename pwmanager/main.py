import os

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal

from controllers.user import User
from controllers.vault import Vault
from pwmanager.core.exc import AppError
from pwmanager.controllers.base import Base
from pwmanager.ext.sqlite_ext import extend_sqlite_db

# configuration defaults
CONFIG = init_defaults('pwmanager')
CONFIG['pwmanager']['db_file'] = os.getcwd() + '/passwd.db'


class MyApp(App):
    """MFM Password Manager primary application."""

    class Meta:
        label = 'pwmanager'

        # configuration defaults
        config_defaults = CONFIG

        hooks = [
            ('post_setup', extend_sqlite_db)
        ]

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            User,
            Vault
        ]


class AppTest(TestApp, App):
    """A sub-class of App that is better suited for testing."""

    class Meta:
        label = 'pwmanager'


def main():
    with MyApp() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except AppError as e:
            print('AppError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except Exception as e:
            print('Exception > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
