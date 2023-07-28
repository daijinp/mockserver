"""
 作者:Dorn
 日期:2023年04月14日,16:27:26
"""
__author__ = 'Dorn'

import uuid

from flask import request
from flask.json import jsonify
from app.utils.redprint import Redprint
from app.utils.data_packet import DataPacket
from app.utils import mock
from app.validators.user_forms import UserForm

api = Redprint('user')


@api.route('/login', methods=['POST'])
def login():
    form = UserForm().validate_for_api()
    token = {'token': '8939005701662415415.TEST.TESTTESTTESTTESTTESTTEST==', 'errno': 0}
    token.update({'account': form.account.data})
    return jsonify(DataPacket().basic(token))


@api.route('/<string:user_id>/info', methods=['GET', 'POST'])
def get_user(user_id):
    user = {'user_id': user_id, 'name': 'tester', 'email': 'tester@test.cn', 'password': "*****"}
    result = {
        'query_params': request.args.to_dict(),
        'path_params': request.view_args,
        'body': request.get_json(silent=True),
        'xy': user
    }
    print( request.get_json())
    return jsonify(DataPacket().basic(result))


@api.route('/simple/list', methods=['POST'])
def simple_list():
    datas = []
    for i in range(1000, 9999):
        datas.append({'id': i, 'name': mock.get_string('username')})
    return jsonify(DataPacket().basic(datas))


@api.route('/<string:role>/info', methods=['POST'])
def get_role(role_id):
    user = {'role_id': role_id, 'name': '角色', 'email': '291691522@qq.com', 'password': "*****"}
    result = {
        'query_params-role_id': request.args.to_dict(),
        'path_params-role_id': request.view_args,
        'body-role_id': request.get_json(silent=True),
        'xy-role_id': user
    }
    return jsonify(DataPacket().basic(result))
