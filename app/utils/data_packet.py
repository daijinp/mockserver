"""
 作者：Dorn
 日期:2023年07月07日,13:26:50
"""
__author__ = 'Dorn'


class DataPacket:
    def basic(self, datas):
        return {'error_code': 0, 'data': datas}

    def list(self, form, data):
        page = form.page.data
        size = form.size.data
        total = len(data)
        res = data[(page - 1) * size: page * size]
        return {'error_code': 0, 'data': res, 'page': page, 'size': size, 'total': total}

