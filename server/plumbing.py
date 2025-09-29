def extract_path_params(route_path, request_path):
    if "<id>" in route_path:
        base_path = route_path.split("<id>")[0]
        if request_path.startswith(base_path):
            id_part = request_path[len(base_path):].split("/")[0]
            return id_part
    return None
