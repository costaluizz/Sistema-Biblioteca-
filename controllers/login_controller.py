from views.login_view import LoginView
from tkinter import messagebox
from models.login_model import Login

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
    
    def verificar_login(self):
        email = self.view.email_var.get()
        senha = self.view.senha_var.get()
        tipo = self.view.tipo_var.get()


        if not email or not senha or not tipo:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios.")
            return

        login = Login(email, senha, tipo)
        usuario = login.consultar_login()

        if usuario:
            messagebox.showinfo("Sucesso", f"Login como {usuario.email} ({tipo})")
           # redircionar painel de emprestimos do aluno
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    def abrir_tela_cadastro(self):
        from controllers.cadastrar_controller import CadastrarController
        self.view.frame.destroy()
        CadastrarController(self.root).mostrar_tela()

