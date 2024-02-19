import configparser
class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.email = self.config['PAGESETTINGS']['email']
        self.date = self.config['PAGESETTINGS']['date']
        self.transaction_amount = self.config['PAGESETTINGS']['transactions']

settings = Settings()
