import tornado.web
from models.users import *

class SignHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sign.html')

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        user = Users.get_or_none(Users.email == email)

        if user:
            result = {"status":"该账号已注册，请前往登陆", "url":"/sign/"}
            self.write(result)
        
        else:
            result = {"status":"success", "url":"/"}
            user = Users.create(username=email, email=email, password=password)
            user.save()
            self.set_secure_cookie("email", str(email))
            self.write(result)
