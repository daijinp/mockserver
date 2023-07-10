"""
 作者:Dorn
 日期:2023年04月19日,19:23:08
"""
__author__ = 'Dorn'

from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        # 如果在实例化的时候传了参数那么就使用传进来的参数
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            # 请求方法 + url(去除问号后面的参数)
            # request=request.method + ' ' + self.get_url_no_param()
            request=f'{request.method}{self.get_url_no_param()}'
        )
        # JSON序列化。序列化成文本
        text = json.dumps(body)
        return text

    # 改写请求头,为了返回的是JSON
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

