import datetime
import random,string

from peewee import *
from .database import database

from pbkdf2 import PBKDF2

class Users(Model):
    username = CharField(unique=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    _password = CharField()
    email = CharField()

    class Meta:
        database = database


    #定义一个内部使用加密的方法
    def _hash_password(self,password):
        return PBKDF2.crypt(password)

    #使用property装饰器使方法变为属性
    @property
    def password(self):
        return self._password

    #设置加密后给类属性赋值
    @password.setter
    def password(self,password):
        self._password = self._hash_password(password)

    #定义一个密码校验的方法
    def auth_password(self,pwd):
        if self._password is not None:
            return self.password == PBKDF2.crypt(pwd, self.password)
        else:
            return False


class InviteCode(Model):
    owner = ForeignKeyField(Users)
    created_date = DateTimeField(default=datetime.datetime.now)
    count = IntegerField(default=0)
    code = TextField()
    class Meta:
        database = database
    
    @property
    def new_code(self):
        return "".join(random.sample(string.ascii_letters + string.digits,12))
