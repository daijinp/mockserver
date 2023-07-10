"""
 作者:Dorn
 日期:2023年4月15日,d

 12:41:53
"""
__author__ = 'Dorn'

from app import create_app

from app.utils.error import APIException
from werkzeug.exceptions import HTTPException
from app.utils.error_code import ServerError, ParameterTypeError
from wsgiref.simple_server import make_server
import waitress

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    """
    @app.errorhandler(Exception)
        此处Flask1.0支持捕捉Exception异常,但是0.12是不支持捕捉所有异常的
    e:
        类型:可能是 APIException、HTTPException、Exception。
            APIException 直接返回
            HTTPException 转换成 APIException 返回


    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        # HTTPException错误信息存在description中
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式,如果在配置文件中读取到是调试模式,那么就返回具体信息。方便开发的时候寻找错误
        if not app.config['DEBUG']:
            if isinstance(e, TypeError):
                return ParameterTypeError()
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    # 开发环境
    app.run(debug=True, port='6000')

    # 生产环境1 (简单的 HTTP 服务器)
    # make_server('0.0.0.0', 5000, app).serve_forever()

    # 生成环境2 (生产级的纯 Python WSGI 服务器，具有非常可观的性能) -->推荐使用<--
    # app.config['DEBUG'] = False
    # waitress.serve(app, host='0.0.0.0', port='5000')
