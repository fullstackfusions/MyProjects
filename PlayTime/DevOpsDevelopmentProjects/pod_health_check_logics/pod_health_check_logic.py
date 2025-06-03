import threading
import socketserver
import http.server as httpServer
from http import HTTPStatus


## HealthCheckHandler is defined in common.utils.health_check as following:
class HealthCheckHandler(httpServer.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def health_response(self):
        return 'healthy'.encode()

    def do_GET(self):
        if self.path in ['/health', 'healthz', '/healthz.html']:
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', str(len(self.health_response)))
            self.end_headers()
            self.wfile.write(bytes(self.health_response))
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', str(0))
            self.end_headers()


def health_check():
    health_server = socketserver.TCPServer(('localhost', 8000), HealthCheckHandler)
    try:
        while threading.main_thread().is_alive():
            health_server.handle_request()
    except KeyboardInterrupt:
        print("Health check server stopped.")
    finally:
        health_server.server_close()
