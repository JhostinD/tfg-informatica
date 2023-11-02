from decouple import RepositoryIni, Config

# Values will be in settings.ini file, not committed to github
config = Config(RepositoryIni("settings.ini"))

# Global consts
DB_PASS = config("DB_PASS")
DB_USER = config("DB_USER")
DB_NAME = config("DB_NAME")