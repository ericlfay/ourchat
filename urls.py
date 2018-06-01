from views.index import MainHandler
from views.sign import  SignHandler
from views.login import LoginHandler, LogoutHandler
from views.ajax import InviteHandler
from views.chat import ChatRoomHandler, ChatHandler

urls = [
(r'/', MainHandler),
(r'/sign/', SignHandler),
(r'/login/', LoginHandler),
(r'/logout/', LogoutHandler),

(r'/get_invide_code/', InviteHandler),

(r'/chat_rooms/', ChatRoomHandler),
(r'/chat/', ChatHandler),
]