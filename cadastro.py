# cadastro.py
import re

class CadastroSystem:
    def __init__(self):
        self.usuarios = {}

    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def cadastrar(self, nome, email, senha):
        if not nome or not email or not senha:
            return "Campos obrigatórios"

        if not self.validar_email(email):
            return "Formato de email inválido"

        if email in self.usuarios:
            return "Email já cadastrado"

        self.usuarios[email] = {"nome": nome, "senha": senha}
        return "Cadastro realizado com sucesso"