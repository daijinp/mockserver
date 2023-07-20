"""
 作者:Dorn
 日期:2023年04月19日,19:23:08
"""
__author__ = 'Dorn'

import uuid

from flask import request
from jsonpath import jsonpath
from wtforms import Form

from app.utils.error_code import ParameterException, CodeError
from wtforms import StringField, IntegerField
from wtforms.validators import length


class BaseForm(Form):

    def __init__(self, data=None):
        self.initialized_datas = request.get_json(silent=True)
        # 表单参数
        args = request.args.to_dict()
        # 路径参数
        args.update(request.view_args)

        if data:
            if not isinstance(data, dict):
                raise CodeError('验证器自定义数据必须是JSON')
            super(BaseForm, self).__init__(data=data, **args)
        else:
            super(BaseForm, self).__init__(data=self.initialized_datas, **args)

    def set_args(self, key=None, value_type=None):
        pass

    def validate_for_api(self):
        # 重写这个方法必须完成原有validate方法
        # 接受结果
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    @staticmethod
    def check_uuid1(_uuid, version=1):
        try:
            return uuid.UUID(_uuid).version == version
        except ValueError:
            raise ParameterException(msg=f'uuid must be a uuid{version}')


class SimpleListForm(BaseForm):
    condition = StringField(validators=[length(min=0, max=128)])

    def validate_condition(self, value):
        if value.data is None:
            value.data = ''
        value.data = f'%{value.data}%'


class ListForm(BaseForm):
    condition = StringField(validators=[length(min=0, max=128)])
    page = IntegerField(validators=[])
    size = IntegerField(validators=[])

    def validate_condition(self, value):
        if value.data is None:
            value.data = ''
        value.data = f'%{value.data}%'

    def validate_page(self, value):
        try:
            value.data = int(value.data)
        except ValueError:
            value.data = 1
            self.size = 10

    def validate_size(self, value):
        self.validate_page(value)

