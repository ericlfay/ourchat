import os
import models
from settings import database

try:
    import psycopg2
    from psycopg2 import extensions as pg_extensions
except ImportError:
    psycopg2 = None

database.create_tables(models.__all__, safe=True)
