import os

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from cement.ext.ext_colorlog import ColorLogHandler

from .controllers.entry import Entry
from .controllers.user import User
from .core.exc import AppError
from .controllers.base import Base
from .ext.json_ext import extend_json_file_db

# configuration defaults
CONFIG = init_defaults('pwmanager', 'log.colorlog')
if not hasattr(CONFIG['pwmanager'], 'db_file'):
    CONFIG['pwmanager']['db_file'] = os.getcwd() + '/../passwd.db'

COLORS = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}


class MyApp(App):
    """MFM Password Manager primary application."""

    class Meta:
        label = 'pwmanager'

        # configuration defaults
        config_defaults = CONFIG

        hooks = [
            # ('post_setup', extend_sqlite_db)
            ('post_setup', extend_json_file_db)
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
        config_files = [
            '/etc/pwmanager/app.conf',
            '~/.config/pwmanager/app.conf',
            '~/Documents/pet-projects/pwManager/config/pwmanager.yml'
        ]

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = ColorLogHandler(colors=COLORS)

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            User,
            Entry
        ]


class MyAppTest(TestApp,MyApp):
    """A sub-class of MyApp that is better suited for testing."""

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
