#!/usr/bin/python

LISTEN_IP = '192.168.0.1'
LISTEN_PORT = 10942

import SocketServer
from pysnarl import PySnarl


def alert(title, msg, timeout=5):
    PySnarl.snShowMessage(title, msg, timeout)


class Server(SocketServer.TCPServer):
    pass


class RequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print("handle request")
        line = self.rfile.readline().strip()
        alert("tcpsnarl", line, 5)


class Main:
    def main(self):
        v = PySnarl.snGetVersion()
        if not v:
            print("Sorry - Snarl does not appear to be running")
            return
        (major, minor) = v
        print("Found Snarl version", str(major) + "." + str(minor), "running.")
        alert("tcpsnarl", "tcpsnarl started")

        self.listen()

    def listen(self):
        Server((LISTEN_IP, LISTEN_PORT), RequestHandler).serve_forever()


if __name__ == '__main__':
    Main().main()

