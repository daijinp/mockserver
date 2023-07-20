"""
 作者:Dorn
 日期:2023年04月14日,16:27:26
"""
__author__ = 'Dorn'

import uuid

from flask.json import jsonify
from app.utils.redprint import Redprint
from app.utils.data_packet import DataPacket
from app.utils import mock
from app.validators.user_forms import UserForm

api = Redprint('user')


@api.route('/login', methods=['POST'])
def login():
    form = UserForm().validate_for_api()
    token = {'token': '8939005701662415415.TEST.TESTTESTTESTTESTTESTTEST==', 'errno':0}
    token.update({'account': form.account.data})
    return jsonify(DataPacket().basic(token))


@api.route('/<string:user_id>/info', methods=['GET'])
def get_user(user_id):
    user = {'user_id': user_id, 'name': 'tester', 'email': 'tester@test.cn', 'password': "*****"}
    return jsonify(DataPacket().basic(user))


@api.route('/simple/list', methods=['POST'])
def simple_list():
    datas = []
    for i in range(1000, 9999):
        datas.append({'id': i, 'name': mock.get_string('username')})
    return jsonify(DataPacket().basic(datas))
