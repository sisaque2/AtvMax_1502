from flask import Flask, jsonify, request

class UsuarioViewWeb:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):
        
        @self.app.route("/", methods=["GET"])
        def mostrar_menu():
            menu_opcoes = {
                "1": "Criar usuário (Faça um POST para /usuarios)",
                "2": "Listar usuários (Faça um GET para /usuarios)",
                "0": "Sair (Não aplicável na web)"
            }
            return jsonify(menu_opcoes)

        @self.app.route("/usuarios", methods=["POST"])
        def criar_usuario():
            dados = request.get_json()  
            nome = dados.get("nome")
            email = dados.get("email")
            
            resposta_controller = self.controller.request_criacao(nome, email)
            
            return jsonify({"status": self.mostrar_mensagem(resposta_controller)})

        @self.app.route("/usuarios", methods=["GET"])
        def listar_usuarios():
            usuarios = self.controller.request_lista()
            return jsonify({"usuarios": usuarios})

    def mostrar_mensagem(self, mensagem):
        return mensagem

    def run(self):
        self.app.run(debug=True)