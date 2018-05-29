import datetime
from peewee import *
from app_settings import database

class Users(Model):
    _id = UUIDField(primary_key=True)
    username = CharField(unique=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    password = CharField()
    email = CharField()

    class Meta:
        database = database
