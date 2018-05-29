import tornado.web
from models.users import *

class SignHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sign.html')

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        user = Users.create(username=email, email=email, password=password)
        user.save()
        self.render('sign.html')