import tornado.web
from models.users import *


class InviteHandler(tornado.web.RequestHandler):
    def get(self):
        email = self.get_secure_cookie("email")
        user = Users.get_or_none(Users.email == email)
        code = InviteCode.get_or_none(InviteCode.owner == user)
        if code:
            if code.count >=5:
                code.code = code.new_code
                code.count = 0
                code.save()
                result = code.code
            else:
                count = code.count
                result = code.code
        else:
            code = InviteCode()
            code.owner=user
            code.code = code.new_code
            code.save()
            result = code.code
        self.write(result)