import re

class LoginSystem:
    def __init__(self):
        self.usuarios = {"teste@exemplo.com": "senha123"}
        self.tentativas = {}

    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def login(self, email, senha):
        if not email or not senha:
            return "Campos obrigatórios"

        if not self.validar_email(email):
            return "Formato de email inválido"

        if self.tentativas.get(email, 0) >= 3:
            return "Conta bloqueada por muitas tentativas"

        if email in self.usuarios and self.usuarios[email] == senha:
            self.tentativas[email] = 0
            return "Login bem-sucedido"
        else:
            self.tentativas[email] = self.tentativas.get(email, 0) + 1
            return "Credenciais inválidas"