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
    :param locations: Location data
    :return:
    """
    class PosterServerMock(BaseHTTPRequestHandler):
        """Mock server definition
            @todo #101:30min Poster server mock refactor. To simplify future poster mock creation refactor
             PosterServerMock as a generic server for postermocks and extends it for each poster method (locations,
             authentications, etc). So we would have a LocationServermock for Locations poster endpoints, AutherverMock
             for authentication endpoints and so on. Base PosterServerMock would just gave the start_server and
             free_port implemetations (maybe them would just be  invoked in PosterServerMock start), and all the
             location data setting in test_sync.py have to be moved for LocationServerMock.
        """
        LOCATIONS_PATTERN = re.compile(r"/clients.getLocations")
        TABLES_PATTERN = re.compile(r"/clients.getTables")
        TOKEN_PATTERN = re.compile(r"/auth/access_token")
        CUSTOMERS_PATTERN = re.compile(r"/clients.getClients")

        def do_GET(self):
            if re.search(self.LOCATIONS_PATTERN, self.path):
                self.send("locations")
                return

            if re.search(self.TABLES_PATTERN, self.path):
                self.send("tables")
                return

            if re.search(self.CUSTOMERS_PATTERN, self.path):
                self.send("customers")
                return

        def send(self, target_type=""):
            self.send_response(requests.codes.ok)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            content = json.dumps(kwargs.get(target_type, {}))
            self.wfile.write(content.encode("utf-8"))

        def do_POST(self):
            if re.search(self.TOKEN_PATTERN, self.path):
                self.send_response(requests.codes.ok)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                content = json.dumps(
                    {
                        "access_token":"861052:02391570ff9af128e93c5a771055ba88",
                        "account_number":"861052",
                        "user":{
                            "id":4,
                            "name":"Mike Haggar",
                            "email":"haggar@metrocity.com",
                            "role_id":3
                        },
                        "ownerInfo":{
                            "email":"haggar@metrocity.com",
                            "phone":"+380684152664",
                            "city":"Metro City",
                            "country":"US",
                            "name":"Mike Haggar",
                            "company_name":"Metro City Administration"
                        },
                        "tariff":{
                            "key":"pricing-plan-1",
                            "next_pay_date":"2020-05-31 11:52:41",
                            "price":2
                        }
                    }
                )
                self.wfile.write(content.encode("utf-8"))
                return

    server = HTTPServer(("localhost", port), PosterServerMock)
    thread = Thread(target=server.serve_forever)
    thread.setDaemon(True)
    thread.start()
