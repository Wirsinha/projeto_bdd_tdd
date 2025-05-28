# teste_cadastro.py
from cadastro import CadastroSystem

def test_cadastro_valido():
    sistema = CadastroSystem()
    resultado = sistema.cadastrar("João", "joao@exemplo.com", "senha123")
    assert resultado == "Cadastro realizado com sucesso"

def test_cadastro_email_existente():
    sistema = CadastroSystem()
    sistema.cadastrar("João", "joao@exemplo.com", "senha123")
    resultado = sistema.cadastrar("Maria", "joao@exemplo.com", "senha456")
    assert resultado == "Email já cadastrado"

def test_cadastro_email_invalido():
    sistema = CadastroSystem()
    resultado = sistema.cadastrar("João", "joaoemail.com", "senha123")
    assert resultado == "Formato de email inválido"

def test_cadastro_campos_obrigatorios():
    sistema = CadastroSystem()
    resultado = sistema.cadastrar("", "", "")
    assert resultado == "Campos obrigatórios"