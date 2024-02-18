import os
from decouple import RepositoryIni, Config

# Values will be in settings.ini file, not committed to github
config = Config(RepositoryIni("settings.ini"))

# Global consts
DB_PASS = config("DB_PASS")
DB_USER = config("DB_USER")
DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")

# Google Cloud Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './tfg-informatica-405322-4dcc7549cb08.json'
