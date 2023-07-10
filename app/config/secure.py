"""
 作者:Dorn
 日期:2023年04月15日,12:28:45
"""

__author__ = 'Dorn'

from app.config import config

DIALECT = 'mysql'
DRIVER = 'cymysql'
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
HOST = config.HOST
PORT = config.PORT
DATABASE = config.DATABASE

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_ECHO = config.SQLALCHEMY_ECHO

# 字符串,保证这个数是一个唯一的字符串
SECRET_KEY = '\x88D\xf09\xa0A\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'


