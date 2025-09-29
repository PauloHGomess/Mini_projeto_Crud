from http.server import HTTPServer, BaseHTTPRequestHandler
from server.router import handle

class Server(HTTPServer):
    def __init__(self, host='localhost', port=8000):
        super().__init__((host, port), RequestHandler)
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def run(self):
        print(f"Servidor rodando em http://localhost:{self.server_port}")
        self.serve_forever()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle(self, self.server, 'GET')

    def do_POST(self):
        handle(self, self.server, 'POST')
