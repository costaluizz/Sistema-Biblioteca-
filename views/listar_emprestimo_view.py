import tkinter as tk
from tkinter import ttk
from controllers.emprestimo_controller import EmprestimoController
from views.menu_principal_view import MenuPrincipalView

class ListarEmprestimosView:
    def __init__(self, usuario_logado):
        self.usuario = usuario_logado 
        self.controller = EmprestimoController()

        self.root = tk.Tk()
        self.root.title("Lista de Empréstimos")
        self.root.geometry("900x500")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        titulo = ttk.Label(self.frame, text="Empréstimos", font=("Helvetica", 16))
        titulo.pack(pady=10)

        self.tabela = ttk.Treeview(
        self.frame,
        columns=("titulo", "data_emprestimo", "data_devolucao"),
        show="headings"
        )
        self.tabela.heading("titulo", text="Título do Livro")
        self.tabela.heading("data_emprestimo", text="Data do Empréstimo")
        self.tabela.heading("data_devolucao", text="Data de Devolução")
        self.tabela.pack(fill=tk.BOTH, expand=True)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.voltar)
        btn_voltar.pack(pady=10)

        self.carregar_dados()

        self.root.mainloop()

    def carregar_dados(self):
        tipo = self.usuario['tipo']
        id_aluno = self.usuario.get('id_aluno')

        emprestimos = self.controller.listar_por_usuario(tipo, id_aluno)

        for emp in emprestimos:
            self.tabela.insert("", "end", values=(
            emp['titulo'], 
            emp['data_emprestimo'], 
            emp['data_devolucao']
        ))

    def voltar(self):
        self.root.destroy()
        MenuPrincipalView(self.usuario)