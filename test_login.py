from login import LoginSystem

def test_login_sucesso():
    sistema = LoginSystem()
    assert sistema.login("teste@exemplo.com", "senha123") == "Login bem-sucedido"

def test_login_senha_errada():
    sistema = LoginSystem()
    assert sistema.login("teste@exemplo.com", "errada") == "Credenciais inválidas"

def test_email_invalido():
    sistema = LoginSystem()
    assert sistema.login("emailsemarroba", "senha123") == "Formato de email inválido"

def test_campos_vazios():
    sistema = LoginSystem()
    assert sistema.login("", "") == "Campos obrigatórios"

def test_bloqueio_tentativas():
    sistema = LoginSystem()
    for _ in range(5):
        sistema.login("teste@exemplo.com", "errada")
    assert sistema.login("teste@exemplo.com", "errada") == "Conta bloqueada por muitas tentativas"