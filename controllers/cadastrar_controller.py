from models.cadastrar_models import Cadastrar
from views.cadastro_aluno_view import CadastroAlunoView
from tkinter import messagebox

class CadastrarController:
    def _init_(self, root):
        self.root = root
        self.view = CadastroAlunoView(self)

    def mostrar_tela(self):
        self.view.mostrar()

    def cadastrar(self, nome, email, senha):
        if not nome or not email or not senha:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")
            return

        novo_aluno = Cadastrar(nome, email, senha)
        novo_aluno.salvar()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")