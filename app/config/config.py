"""
 作者:Dorn
 日期:2023年04月15日,12:27:09
"""

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'test'
PASSWORD = 'test'
HOST = 'test'
PORT = 'test'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# 是否打印SQL语句
SQLALCHEMY_ECHO = False

# 编码
SQLALCHEMY_ENCODING = "utf8mb4"

# DEBUG打开,和manager中的DEBUG负责的东西不太一样，这里是不能让 app.logger.info(i.name)生效的。
# DEBUG = True

# DebugToolbarExtension 需要的配置
SECRET_KEY = "pp.up"

# print(SQLALCHEMY_DATABASE_URI)


