#!/usr/bin/env python
#
# This is a basic web server that serves a listing of the current directory and any files inside.
#
import SimpleHTTPServer
import SocketServer
import logging

PORT = 8000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
