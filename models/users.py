import datetime
from peewee import *
# from settings import database
database = PostgresqlDatabase(
    'ddvofnab',
    user='ddvofnab',
    password='zL26CJ8avpFnpOag3ke2v29laiq7F8GX',
    host='pellefant.db.elephantsql.com',
    port=5432,)
database.connect()

class Users(Model):
    username = CharField(unique=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    password = CharField()
    email = CharField()

    class Meta:
        database = database
