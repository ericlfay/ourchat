#coding:utf-8
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("email")
        if cookie:
        	self.render('index.html')
        else:
        	self.redirect("/login/")