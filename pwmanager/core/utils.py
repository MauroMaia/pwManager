import hashlib
import datetime
import uuid
import requests

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


def check_for_password_exploits(app, password: str):
    password_hash = hashlib.sha1(bytes(password, 'utf-8')).hexdigest().upper()
    hash5sum = password_hash[:5]

    url = "https://api.pwnedpasswords.com/range/" + hash5sum

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    hashlist = response.text.split('\r\n')

    app.log.debug("Checking password against 'pwnedpasswords' database.")
    for hash_password in hashlist:
        if password_hash.find(hash_password.split(':')[0]) >= 0:
            app.log.warning("This password has been pwned")
            return True

    return False
