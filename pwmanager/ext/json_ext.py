from ext.persistence.json.json_file_db import JsonFileDB


def extend_json_file_db(app):
    app.log.info('extending todo application with Json File database')
    db_file = app.config.get('pwmanager', 'db_file')

    app.log.debug('Creating database connection')
    db = JsonFileDB(db_file)

    app.extend('db', db)
