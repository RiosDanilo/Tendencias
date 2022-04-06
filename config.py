from distutils.command.config import config
from distutils.debug import DEBUG


class DevelopmentConfig():
    debug = True
    MYSQL_Host = 'localhost'
    MYSQL_User = 'danilo'
    MYSQL_Password = '12345'
    MySQL_db = 'deporte'


config = {
    'development' : DevelopmentConfig
}