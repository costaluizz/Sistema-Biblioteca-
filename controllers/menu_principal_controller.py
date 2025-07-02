from views.menu_principal_view import MenuPrincipalView
from tkinter import messagebox

class MenuPrincipalController:
    def __init__(self, root, tipo_usuario):
        self.root = root
        self.tipo_usuario = tipo_usuario
        self.view = MenuPrincipalView(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
        
    def sair(self):
        from controllers.login_controller import LoginController
        self.view.frame.destroy()
        LoginController(self.root).iniciar_login()
        
    def abrir_cadastro_alunos(self):
        from controllers.cadastrar_controller import CadastrarController
        self.view.frame.destroy()
        CadastrarController(self.root).mostrar_tela()
        
    def abrir_cadastro_livros(self):
        from controllers.livro_controller import LivroController
        self.view.frame.destroy()
        LivroController(self.root).iniciar_tela()
        

