import os
import models
from models.database import database
from settings import logger

try:
    database.create_tables(models.__all__, safe=True)
    logger.info("All tables created !")
except:
    logger.info("All tables failed !")
    