from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import socket
from threading import Thread

import requests


def free_port():
    """Returns free port

    :return: Port
    """
    sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(("localhost", 0))
    address, port = sock.getsockname()
    sock.close()
    return port

def start_server(port, **kwargs):
    """Starts Poster mock server
    :param port: Port
    :param kwargs:
        locations: Location data
    :return:
    """
    class PosterServerMock(BaseHTTPRequestHandler):
        """Mock server definition

        """
        LOCATIONS_PATTERN = re.compile(r"/clients.getLocations")
        TABLES_PATTERN = re.compile(r"/clients.getTables")

        def do_GET(self):
            if re.search(self.LOCATIONS_PATTERN, self.path):
                self.send("locations")
                return
            if re.search(self.TABLES_PATTERN, self.path):
                self.send("tables")
                return


        def send(self, target_type=""):
            self.send_response(requests.codes.ok)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            content = json.dumps(kwargs.get(target_type, {}))
            self.wfile.write(content.encode("utf-8"))


    server = HTTPServer(("localhost", port), PosterServerMock)
    thread = Thread(target=server.serve_forever)
    thread.setDaemon(True)
    thread.start()