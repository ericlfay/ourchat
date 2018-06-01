import tornado.web
from models.users import *

class SignHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("email", None)
        if cookie:
            self.redirect("/")
        else:
            self.render('sign.html')
        

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        code = self.get_argument('code', None)
        user = Users.get_or_none(Users.email == email)
        
        if code:
            coder = InviteCode.get_or_none(InviteCode.code == code)
            if coder:
                count = coder.count
                if count >=5:
                    coder.code = coder.new_code
                    coder.count = 0
                    coder.save()
                else:
                    coder.count = count + 1
                    coder.save()
                if user:
                    result = {"status":"该账号已注册，请前往登陆", "url":"/sign/"}
                    self.write(result)
                
                else:
                    result = {"status":"success", "url":"/"}
                    user = Users.create(username=email, email=email, password=password)
                    user.save()
                    self.set_secure_cookie("email", str(email))
                    self.write(result)
            else:
                result = {"status":"请输入正确的邀请码！", "url":"/sign/"}
                self.write(result)

        else:
                result = {"status":"请输入邀请码！", "url":"/sign/"}
                self.write(result)
