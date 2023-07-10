"""
 作者：Dorn
 日期:2023年04月16日,23:38:18
"""
__author__ = 'Dorn'

from app.utils.error_code import NotFound, DataAssociationException, CodeError
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import inspect, Column, Integer, SmallInteger, orm, String
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


"""
    Query覆盖了查询类,为了重写filter_by
"""


class Query(BaseQuery):
    def filter_by(self, *args, **kwargs):
        """
            添加了status=0,剔除了被逻辑删除的数据
        """
        try:
            [kwargs.update(arg) for arg in args]
        except TypeError:
            raise CodeError(msg="code error:filter_by")
        if 'status' not in kwargs.keys():
            kwargs.update({'status': 0})
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        """
            ident是主键字段的值
            在query()之后调用,会查询主键的值是否等于ident
                    如果未查询到数据,则报错 404 NotFound
                    如果查询到数据, 则return数据
            这个方法重写的原因是修改原本框架的报错方式,否则报错HTML
        """
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self, msg=None):
        """
            在filter_by()之后调用,
                如果未查询到数据,则报错 404 NotFound
                如果查询到数据, 则return第一条数据
            这个方法重写的原因是修改原本框架的报错方式,否则报错HTML
        """
        rv = self.first()
        if not rv:
            raise NotFound(msg=msg)
        return rv

    def first_is_null(self, msg=None):
        """
            在filter_by()之后调用
                如果在filter_by()中的条件查询到了数据, 则报错。如果无数据就不会报错
        """
        rv = self.first()
        if rv:
            raise DataAssociationException(msg=msg)


# 实例化SQLAlchemy对象
db = SQLAlchemy(query_class=Query)

"""
    Base模型的基类
        为所有的模型添加了、create_time、status这两个属性
        添加所有模型一些公共的方法。例如 删除一个模型: delete
"""


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    # 逻辑删除: 0 未删除, 1 删除
    status = Column(SmallInteger, default=0)
    create_time = Column(String(24))

    def __init__(self):
        # self.create_time = int(datetime.now().timestamp())
        self.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self

    def reserve(self, *keys):
        removed = set(self.fields) - set(keys)
        [self.fields.remove(i) for i in removed]
        return self

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete_hide(self):
        self.status = 1


# 这是一个更加方便的序列化器,可以将一个模型下定义的所有字段全部读取出来;
class MixinJSONSerializer:
    @orm.reconstructor
    def init_on_load(self):
        self._fields = []
        # self._include = []
        self._exclude = []

        self._set_fields()
        self.__prune_fields()

    def _set_fields(self):
        pass

    def __prune_fields(self):
        columns = inspect(self.__class__).columns
        if not self._fields:
            all_columns = set(columns.keys())
            self._fields = list(all_columns - set(self._exclude))

    def hide(self, *args):
        for key in args:
            self._fields.remove(key)
        return self

    def keys(self):
        return self._fields

    def __getitem__(self, key):
        return getattr(self, key)
