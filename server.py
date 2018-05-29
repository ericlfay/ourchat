#coding:utf-8
import tornado.ioloop
import sys
from settings import settings
PORT = '8080'
if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
settings.listen(PORT)
print ('Development server is running at http://127.0.0.1:%s/' % PORT)
print ('Quit the server with CONTROL-C or CONTROL-BREAK')
tornado.ioloop.IOLoop.instance().start()