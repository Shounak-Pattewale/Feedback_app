import os

# Default configurations are common across environments
class DefaultConfig(object):
    # Machine Configuration
    HOST_MACHINE_IP = '0.0.0.0'

    HOST_MACHINE_PORT = 5001

    BACKEND_API_MACHINE_URL = 'http://127.0.0.1:5000'

    # Debug Configuration
    DEBUG = False

    # Session Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_KEY = os.environ.get('SESSION_KEY')

    SERVICE_ACCOUNT_JSON = os.environ.get('SERVICE_ACCOUNT_JSON')