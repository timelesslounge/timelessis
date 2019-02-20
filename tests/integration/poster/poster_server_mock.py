from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import socket
import requests
from threading import Thread
from http.server import  HTTPServer
import json


class PosterServerMock(BaseHTTPRequestHandler):
    """Generic Mock for Poster interactions"""

    PATTERN = None
    port = None

    def start(self):
        self.port = self.free_port(self)
        server = HTTPServer(("localhost", self.port), self)
        thread = Thread(target=server.serve_forever)
        thread.setDaemon(True)
        thread.start()

    def free_port(self):
        """Returns free port

        :return: Port
        """
        sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        sock.bind(("localhost", 0))
        address, port = sock.getsockname()
        sock.close()
        return port

    def do_GET(self):
        if re.search(self.PATTERN, self.path):
            self.send_response(requests.codes.ok)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(self.get_content().encode("utf-8"))
            return
        else:
            self.send_response(requests.codes.not_found)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

    def do_POST(self):
        if re.search(self.PATTERN, self.path):
            self.send_response(requests.codes.ok)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(self.post_content().encode("utf-8"))
            return
        else:
            self.send_response(requests.codes.not_found)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

    def get_content(self):
        return json.dumps("get content")

    def post_content(self):
        return json.dumps("post content")

