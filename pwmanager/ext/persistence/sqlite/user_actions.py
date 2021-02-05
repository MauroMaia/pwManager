from .db_models import AppUsers


def find_user_by_name(app, username):
    try:
        return app.db.query(AppUsers).filter_by(
            username=username
        ).one()
    except Exception as e:
        app.log.debug('Exception, {}'.format(e.__cause__))
        return None


def find_user_by_name_and_hash(app, username, hash):
    try:
        return app.db.query(AppUsers).filter_by(
            username=username,
            password_hash=hash
        ).one()
    except Exception as e:
        app.log.debug('Exception, {}'.format(e.__cause__))
        return None


def delete_user(app, username, hash):
    db_user = find_user_by_name_and_hash(app, username, hash)
    if db_user is not None:
        app.db.delete(db_user)
        app.db.commit()
        app.log.info('User deleted')
    else:
        app.log.error('Unable to delete the user')
