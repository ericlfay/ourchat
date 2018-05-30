from views.index import MainHandler
from views.sign import  SignHandler
from views.login import LoginHandler, LogoutHandler

urls = [
(r'/', MainHandler),
(r'/sign/', SignHandler),
(r'/login/', LoginHandler),
(r'/logout/', LogoutHandler),
]