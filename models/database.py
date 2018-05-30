from peewee import *
from playhouse.db_url import connect

try:
    import psycopg2
    from psycopg2 import extensions as pg_extensions
except ImportError:
    psycopg2 = None

database = PostgresqlDatabase(
    'ddvofnab',
    user='ddvofnab',
    password='zL26CJ8avpFnpOag3ke2v29laiq7F8GX',
    host='pellefant.db.elephantsql.com',
    port=5432,)
database.connect()
