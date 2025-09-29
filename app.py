from server import Server
from routes.usuarios import listar_usuarios, novo_usuario, editar_usuario, excluir_usuario

app = Server()

app.route("/usuarios")(listar_usuarios)
app.route("/usuarios/novo")(novo_usuario)
app.route("/usuarios/<id>/editar")(editar_usuario)
app.route("/usuarios/<id>/excluir")(excluir_usuario)

if __name__ == "__main__":
    print(f"Servidor rodando em http://localhost:{app.server_port}")
    app.serve_forever()
