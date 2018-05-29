# coding:utf-8
import os
import logging
import datetime
from urls import urls

import tornado.web

from peewee import *
from playhouse.db_url import connect

try:
    import psycopg2
    from psycopg2 import extensions as pg_extensions
except ImportError:
    psycopg2 = None


today = datetime.date.today()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('./log/log %s.log' % today)
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

settings = tornado.web.Application(
    handlers=urls,
    **SETTINGS
)


database = PostgresqlDatabase(
    'ddvofnab',
    user='ddvofnab',
    password='zL26CJ8avpFnpOag3ke2v29laiq7F8GX',
    host='pellefant.db.elephantsql.com',
    port=5432,)

try:
    database.connect()
    logger.info('Database connected !')
except(OperationalError, TypeError) as error:
    logger.error('''Database connect failed!  
        Error is 
            %s''' % error)

