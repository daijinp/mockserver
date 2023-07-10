"""
 作者:Dorn
 日期:2023年04月14日,16:27:26
"""
__author__ = 'Dorn'


from flask.json import jsonify
from app.utils.redprint import Redprint
from app.utils.data_packet import DataPacket

api = Redprint('user')


@api.route('/info', methods=['GET'])
def get_user():
    user = {'name': 'tester', 'email': 'tester@test.cn', 'password': "*****"}
    return jsonify(DataPacket().basic(user))
