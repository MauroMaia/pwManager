from .persistence.sqlite.database import Database


def extend_sqlite_db(app):
    app.log.info('extending todo application with sqlite database')
    db_file = app.config.get('pwmanager', 'db_file')

    app.log.debug('Creating database connection')
    engine = Database.connect_to_database(app, db_file)

    app.log.info('Creating new session to database: {}'.format(db_file))
    app.extend('db', engine.new_session())

    # app.log.debug('Checking if database have any users')
    # app_users_size = len(args.db_session.query(AppUsers).all())
