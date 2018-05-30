# coding:utf-8
import os
import logging
import datetime
from urls import urls

import tornado.web

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
setting = {
    "cookie_secret": "bZJc2sWbQLKos6GkHn/AB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
}
settings = tornado.web.Application(
    handlers=urls,
    **SETTINGS,
    **setting,
)


