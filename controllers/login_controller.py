from views.login_view import LoginView
from tkinter import messagebox
from models.login_model import Login
from views.listar_emprestimo_view import ListarEmprestimosView

class LoginController:
    def __init__(self, root):
        self.root = root
        self.view = LoginView(self.root, self)
    
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
            # Fecha a tela de login
            self.view.frame.destroy()

            # Redireciona para ListarEmprestimosView, passando o usuário logado
            usuario_logado = {
                "tipo": tipo,
                "id_aluno": usuario.id if tipo == "aluno" else None
            }
            ListarEmprestimosView(self.root, usuario_logado)

        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    def _abrir_painel_principal(self, tipo):
        from controllers.menu_principal_controller import MenuPrincipalController
        self.view.frame.destroy()
        MenuPrincipalController(self.root, tipo).iniciar_tela()

    def abrir_tela_cadastro(self):
        from controllers.cadastrar_controller import CadastrarController
        self.view.frame.destroy()
        CadastrarController(self.root).mostrar_tela()

    def sair(self):
        self.root.quit()