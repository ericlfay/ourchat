
import tornado.web
from models.users import *


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        user = Users.get_or_none(Users.email == email)
        
        if user:
            is_password = user.auth_password(password)
            if is_password:
                result = {"status":"success", "url":"/"}
                self.set_secure_cookie("email", str(email))
                self.write(result)
            else:
                result = {"status":"密码输入错误！", "url":"/login/"}
                self.write(result)
        
        else:
            result = {"status":"该账号还未注册，请确定输入是否正确！", "url":"/login/"}
            self.write(result)

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("email")
        self.redirect("/")