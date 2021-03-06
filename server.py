
import tornado
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("This is your response")
        self.finish()

app = tornado.web.Application([
    (r"/()$", tornado.web.StaticFileHandler, {'path': 'static/index.html'}),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': 'static/'}),
], debug=True)

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.autoreload.start()
    tornado.autoreload.watch('./**/*')
    tornado.ioloop.IOLoop.instance().start()
