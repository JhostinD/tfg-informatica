from decouple import RepositoryIni, Config

# Values will be in settings.ini file, not committed to github
config = Config(RepositoryIni("settings.ini"))

# Examples that can be taken into account for global vars
# CLIENT_ID = config("CLIENT_ID")
# CLIENT_SECRET = config("CLIENT_SECRET")