import random
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2

BLOCK_SIZE = 16
pad = lambda s: s[:-ord(s[len(s) - 1:])]
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
SALT = b""

# ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')
ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789')


def generate_random_password(app, length):
    app.log.debug('Generate random password with an ALPHABET consisted with: ' + str(ALPHABET))

    chars = []

    while len(chars) < length:
        n = random.randint(0, len(ALPHABET) - 1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha) - 1)
        chars.append(alpha[n])

    return ''.join(chars)


def encrypt(raw, password):
    private_key = _get_private_key(password)
    raw = _pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc, password):
    private_key = _get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[16:]))


def _get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def _pad(s):
    return bytes(s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE), 'utf-8')


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]
