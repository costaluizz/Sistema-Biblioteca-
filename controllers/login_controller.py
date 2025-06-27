from models.login_model import Login

class LoginController:
    @staticmethod
    def consultar():
        email = 'luiz@gmail.com'
        senha = '123456'
        tipo = 'aluno'  

        login = Login(email, senha, tipo)
        usuario = login.consultar_login()

        if usuario:
            print(f"Logado com: {usuario.email}")
            return True
        else:
            print("Email ou senha incorretos.")
            return False