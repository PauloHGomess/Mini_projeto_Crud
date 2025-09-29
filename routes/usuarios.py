import os
from urllib.parse import parse_qs

CAMINHO_ARQUIVO = "usuarios.txt"

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    usuarios = []
    for linha in linhas:
        if linha.strip():
            partes = linha.strip().split("|")
            usuarios.append({
                "id": int(partes[0]),
                "nome": partes[1],
                "email": partes[2],
                "telefone": partes[3],
            })
    return usuarios

def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        for u in usuarios:
            linha = f"{u['id']}|{u['nome']}|{u['email']}|{u['telefone']}\n"
            f.write(linha)

def listar_usuarios(request, response):
    usuarios = carregar_usuarios()
    html = "<h1>Lista de Usuários</h1><ul>"
    for u in usuarios:
        html += f"<li>{u['nome']} - <a href='/usuarios/{u['id']}/editar'>Editar</a> - <a href='/usuarios/{u['id']}/excluir'>Excluir</a></li>"
    html += "</ul><a href='/usuarios/novo'>Novo usuário</a>"

    response.send_response(200)
    response.send_header("Content-type", "text/html; charset=utf-8")
    response.end_headers()
    response.wfile.write(html.encode("utf-8"))

def novo_usuario(request, response):
    if request.command == "GET":
        html = """
        <h1>Novo Usuário</h1>
        <form method="POST">
            Nome: <input type="text" name="nome"><br>
            Email: <input type="text" name="email"><br>
            Telefone: <input type="text" name="telefone"><br>
            <button type="submit">Salvar</button>
        </form>
        """
        response.send_response(200)
        response.send_header("Content-type", "text/html; charset=utf-8")
        response.end_headers()
        response.wfile.write(html.encode("utf-8"))

    elif request.command == "POST":
        tamanho = int(request.headers.get('Content-Length', 0))
        dados = request.rfile.read(tamanho).decode()
        params = parse_qs(dados)

        nome = params.get("nome", [""])[0]
        email = params.get("email", [""])[0]
        telefone = params.get("telefone", [""])[0]

        usuarios = carregar_usuarios()
        novo_id = max([u["id"] for u in usuarios], default=0) + 1

        usuarios.append({
            "id": novo_id,
            "nome": nome,
            "email": email,
            "telefone": telefone
        })

        salvar_usuarios(usuarios)

        response.send_response(303)
        response.send_header("Location", "/usuarios")
        response.end_headers()

def excluir_usuario(request, response, id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if not usuario:
        response.send_response(404)
        response.end_headers()
        response.wfile.write("Usuário não encontrado".encode("utf-8"))
        return

    if request.command == "GET":
        html = f"""
        <h1>Excluir Usuário</h1>
        <p>Tem certeza que deseja excluir {usuario['nome']}?</p>
        <form method="POST">
            <button type="submit">Confirmar Exclusão</button>
        </form>
        <a href="/usuarios">Cancelar</a>
        """
        response.send_response(200)
        response.send_header("Content-type", "text/html; charset=utf-8")
        response.end_headers()
        response.wfile.write(html.encode("utf-8"))
    elif request.command == "POST":
        usuarios = [u for u in usuarios if u["id"] != id]
        salvar_usuarios(usuarios)
        response.send_response(303)
        response.send_header("Location", "/usuarios")
        response.end_headers()

def editar_usuario(request, response, id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if not usuario:
        response.send_response(404)
        response.end_headers()
        response.wfile.write("Usuário não encontrado".encode("utf-8"))
        return

    if request.command == "GET":
        html = f"""
        <h1>Editar Usuário</h1>
        <form method="POST">
            Nome: <input type="text" name="nome" value="{usuario['nome']}"><br>
            Email: <input type="text" name="email" value="{usuario['email']}"><br>
            Telefone: <input type="text" name="telefone" value="{usuario['telefone']}"><br>
            <button type="submit">Salvar Alterações</button>
        </form>
        <a href="/usuarios">Cancelar</a>
        """
        response.send_response(200)
        response.send_header("Content-type", "text/html; charset=utf-8")
        response.end_headers()
        response.wfile.write(html.encode("utf-8"))
    elif request.command == "POST":
        tamanho = int(request.headers.get('Content-Length', 0))
        dados = request.rfile.read(tamanho).decode()
        params = parse_qs(dados)

        usuario["nome"] = params.get("nome", [""])[0]
        usuario["email"] = params.get("email", [""])[0]
        usuario["telefone"] = params.get("telefone", [""])[0]

        salvar_usuarios(usuarios)

        response.send_response(303)
        response.send_header("Location", "/usuarios")
        response.end_headers()
