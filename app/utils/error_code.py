"""
 作者:Dorn
 日期:2023年04月19日,19:23:08
"""
__author__ = 'Dorn'
from werkzeug.exceptions import HTTPException

from app.utils.error import APIException


# ===========================成功

class Success(APIException):
    code = 200
    msg = 'success'
    error_code = 0


# class DeleteSuccess(Success):
#     code = 202
#     error_code = -1

# =========================== 请求参数错误: 1xxx

class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1001


class ParameterTypeError(APIException):
    code = 400
    msg = 'parameter type error'
    error_code = 1002


class ParameterKeyError(APIException):
    code = 400
    msg = 'json key error'
    error_code = 1003


class MethodError(APIException):
    code = 400
    msg = 'unsupported request method'
    error_code = 1051

# =========================== 客户端数据错误:2xxx


class AuthFailed(APIException):
    code = 401
    error_code = 2001
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 2002
    msg = 'forbidden, not in scope'


class TokenInvalid(APIException):
    code = 401
    error_code = 2003
    msg = 'token is expired'

# =========================== 客户端的数据与服务端数据不匹配导致的错误:3xxx


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 3001


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 3002


class DataException(APIException):
    code = 400
    msg = 'invalid data'
    error_code = 3003


class UniqueException(APIException):
    code = 400
    msg = 'not unique data'
    error_code = 3004


class DataAssociationException(APIException):
    code = 400
    msg = 'the data is associated'
    error_code = 3005

# ====================服务器异常类


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class CodeError(ServerError):
    code = 500
    msg = 'known exception, please contact the developer'
    error_code = 999


# ====================客户端配置错误类 10000+
class ConfigError(APIException):
    code = 500
    msg = 'data configuration error '
    error_code = 10000
