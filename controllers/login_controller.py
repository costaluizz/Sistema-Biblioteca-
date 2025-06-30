from views.login_view import LoginView

class LoginController:

    def __init__(self, root):
        self.root = root
        self.view = LoginView(self)
    
    
    '''
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
    '''
    def iniciar_login(self):
        self.view.mostrar()
    

