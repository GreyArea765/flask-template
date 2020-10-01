import os

# Get the base directory of the app.
basedir = os.path.abspath(os.path.dirname(__file__))

# Configurable environment 
class Config(object):
    # Check for secret key environment variable or set it to some default value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key'

    # Check for a remote database configuration or set to local sqlite db.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    # Disable Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # E-Mail alert configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['some@email.local']