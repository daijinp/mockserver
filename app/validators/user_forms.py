"""
 作者：Dorn
 日期:2023年07月10日,18:40:07
"""
__author__ = 'Dorn'

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms import ValidationError

from app.models.base import db
from sqlalchemy import and_

from app.validators.base import BaseForm


class UserForm(BaseForm):
    # 账号
    account = StringField(validators=[DataRequired(message='必填参数,不可为空。'), length(min=5, max=32)])
    # 密码
    password = StringField(validators=[DataRequired(message='必填参数,不可为空。'), length(min=6, max=32)])
