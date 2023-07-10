"""
 作者:Dorn
 日期:2023年04月14日,16:46:43
"""
__author__ = 'Dorn'

from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.utils.error_code import CodeError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # 保证这个属性有keys和__getitem__方法,否则不使用dict
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        """
        如果Python遇到了不能被序列化的对象,就会递归调用default函数的。
        例如被序列号的模型中有一个o.strftime('%Y-%m-%d'),这时候就不能被序列化了，则会第二次调用。
        所以在这里加了一个这个判断。
        所以,如果遇到不能被序列化的对象之后,在这里就要添加更多的处理
        """
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise CodeError(msg='对象反序列化失败')


class Flask(_Flask):
    json_encoder = JSONEncoder
