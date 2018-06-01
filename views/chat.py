import json
import datetime
import tornado.web
from tornado.websocket import WebSocketHandler

class ChatHandler(WebSocketHandler):

    users = set()  # 用来存放在线用户的容器
    user_username = None

    def open(self):
        self.user_username = self.get_secure_cookie("email")
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息
            message = str(self.user_username.decode("utf-8"))
            time =  datetime.datetime.now().strftime("%H:%M:%S")

            u.write_message(json.dumps({'message': message, "time":time}))

    def on_message(self, message):
        self.user_username = self.get_secure_cookie("email")
        for u in self.users:  # 向在线用户广播消息
            u.write_message("%s-%s-说：%s" % (str(self.user_username.decode("utf-8")), datetime.datetime.now().strftime("%H:%M"), message))

    def on_close(self):
        self.user_username = self.get_secure_cookie("email")
        self.users.remove(self) # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message("%s-%s-离开聊天室" % (str(self.user_username.decode("utf-8")), datetime.datetime.now().strftime("%H:%M")))

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


class ChatRoomHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('indextemp/chat_room.html')
