"""
 作者:Dorn
 日期:2023年04月14日,16:37:31
"""
__author__ = 'Dorn'

from flask import Blueprint

from app.api.v1.user import user


def create_blueprint_v1():
    # __name__接受一个位置参数
    bp_v1 = Blueprint('v1', __name__)

    # 红图向蓝图v1的注册
    user.api.register(bp_v1)

    return bp_v1
