from views.index import MainHandler
from views.sign import  SignHandler
from views.login import LoginHandler, LogoutHandler
from views.ajax import InviteHandler

urls = [
(r'/', MainHandler),
(r'/sign/', SignHandler),
(r'/login/', LoginHandler),
(r'/logout/', LogoutHandler),
(r'/get_invide_code/', InviteHandler),
]