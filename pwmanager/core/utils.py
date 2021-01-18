import hashlib
import datetime
import uuid
from getpass import getpass


def create_hash_password(password, username):
    vault_key = hashlib.pbkdf2_hmac(
        'sha256',
        bytes(password, 'utf-8'),
        bytes(username, 'utf-8'),
        10 * 100 * 100
    ).hex()
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        bytes(vault_key, 'utf-8'),
        bytes(password, 'utf-8'),
        10 * 100 * 100
    ).hex()
    return [vault_key, password_hash]


def read_master_password(app):
    counter = 0
    while counter != 3:
        counter += 1

        app.log.debug('Requesting master password. Try ' + str(counter))
        password = getpass('Please provide the master password (size > 8): ')
        if password != '' and len(password) >= 8:
            return password

    app.log.error('No valid master password read. Number of tries: ' + str(counter))
    return None


def json_default(value):
    if isinstance(value, datetime.date):
        return value.astimezone().replace(tzinfo=datetime.timezone.utc).isoformat()
    elif isinstance(value, uuid.UUID):
        return str(value)
    else:
        return value.__dict__
