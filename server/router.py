import re

def handle(request, app, method):
    path = request.path
    for route_path, handler in app.routes.items():
        path_regex = '^' + re.sub(r'<\w+>', r'(\\d+)', route_path) + '$'
        match = re.match(path_regex, path)
        if match:
            params = match.groups()
            if params:
                handler(request, request, *[int(p) for p in params])
            else:
                handler(request, request)
            return
    request.send_response(404)
    request.end_headers()
    request.wfile.write("Rota não encontrada.".encode("utf-8"))
