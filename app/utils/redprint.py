"""
 作者:Dorn
 日期:2023年04月14日,16:21:27
"""
__author__ = 'Dorn'


class Redprint:
    def __init__(self, name):
        """
            name:红图的名字
        """
        self.name = name
        self.mound = []

    """
        定义route装饰器,参照蓝图的书写方式
         **options: 可以添加一些关键字参数,例如methods=['GET','POST']
         
         decorator函数:
            f就是调用装饰器的方法
            不能像蓝图那样获取一些东西,所以先把一些属性保存在mound中,延迟到注册的时候处理
            
         register:
         options.pop("endpoint", f.__name__)
         options是一个字典
         pop是取出字典中的值，并且从字典中把这个值删除
         精妙的地方是，f.__name__的默认值，如果有endpoint就会使用使用endpoint.value，如果没有就会使用视图函数作为endpoint的值。
    """
    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            # endpoint = options.pop("endpoint", f.__name__)
            # endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            endpoint = f'{self.name}+{options.pop("endpoint", f.__name__)}'
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

