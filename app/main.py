import os
import tornado
import tornado.web
from tornado import ioloop
from tornado import httpserver
from tornado.options import define
from tornado.options import options
from handlers import IndexHandler
from handlers import CorrectionHandler
from correction import *


define("port", default=8080, help="run on given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
     handlers=[(r'/', IndexHandler), ('/autocorrect', CorrectionHandler)],
     template_path=os.path.join(os.path.dirname(__file__),
                                "../client/templates"),
     static_path=os.path.join(os.path.dirname(__file__), "../client/static"),
     auto_correct=AutoCorrect())
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()
