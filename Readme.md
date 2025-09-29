# CRUD de Usuários com Servidor HTTP em Python

## 📖 Descrição
Projeto simples de um **CRUD de usuários** (Create, Read, Update, Delete), implementado em **Python puro** usando apenas a biblioteca padrão `http.server`.  
A ideia é construir um servidor HTTP manualmente, sem frameworks externos, com foco didático.

---

## ⚙️ Funcionalidades
- 📄 Listar usuários  
- ➕ Criar usuário  
- ✏️ Editar usuário  
- ❌ Excluir usuário  
- 💾 Persistência básica em arquivo texto (`usuarios.txt`)  

---

## 📂 Estrutura do Projeto
.
├── app.py          # Arquivo principal com o servidor HTTP  
├── usuarios.txt    # "Banco de dados" simples em arquivo texto  
└── README.md       # Este arquivo  

---

## 🚀 Como rodar

1. Certifique-se de ter **Python 3.12+** instalado.  
2. (Opcional) Crie e ative um ambiente virtual:  
   
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate

3. Execute o servidor:
   python app.py

4. Abra no navegador:
   http://localhost:8000/usuarios
