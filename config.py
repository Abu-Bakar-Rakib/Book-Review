import os

basedir = os.path.abspath(os.path.dirname(__file__))


def _get_secret_key():
    """Load or generate a persistent secret key so sessions survive restarts."""
    key_file = os.path.join(basedir, '.secret_key')
    if os.path.exists(key_file):
        with open(key_file, 'r') as f:
            return f.read().strip()
    key = os.urandom(32).hex()
    with open(key_file, 'w') as f:
        f.write(key)
    return key


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or _get_secret_key()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False