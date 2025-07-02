from models.cadastrar_models import Cadastrar
from views.cadastro_aluno_view import CadastroAlunoView
from tkinter import messagebox

class CadastrarController:
    def __init__(self, root):
        self.root = root
        self.view = CadastroAlunoView(self.root, self)
        

    def mostrar_tela(self):
        self.view.mostrar()

    def cadastrar(self, nome, email, senha):
        if not nome or not email or not senha:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")
            return False

        try:
            novo_aluno = Cadastrar(nome=nome, email=email, senha=senha)
            novo_aluno.salvar_cadastrar()
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            self.view.limpar_campos()
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar: {str(e)}")
            return False