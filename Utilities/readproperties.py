import configparser #already in python

config=configparser.RawConfigParser() # create object to access methods
config.read(".\\Configuration\\Config.ini") # to read data from config.ini file

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info used by each Test case','baseURL')
        return url
    @staticmethod
    def getUsermail():
        username = config.get('common info used by each Test case', 'username')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info used by each Test case','password')
        return password