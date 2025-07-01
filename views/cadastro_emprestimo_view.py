import tkinter as tk
from controllers.emprestimo_controller import EmprestimoController

class CadastroEmprestimoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)

        self.livro_var = tk.StringVar()
        self.data_emprestimo_var = tk.StringVar()
        self.data_devolucao_var = tk.StringVar()

    def mostrar(self):
        self.root.title("Cadastro de Empréstimo")
        self.frame.pack(padx=20, pady=20)


        tk.Label(self.frame, text="Livro:").pack()
        tk.Entry(self.frame, textvariable=self.livro_var).pack(pady=5)

        tk.Label(self.frame, text="Data de Empréstimo:").pack()
        tk.Entry(self.frame, textvariable=self.data_emprestimo_var).pack(pady=5)

        tk.Label(self.frame, text="Data de Devolução:").pack()
        tk.Entry(self.frame, textvariable=self.data_devolucao_var).pack(pady=5)

        tk.Button(self.frame, text="Cadastrar", command=self.enviar_cadastro).pack(pady=10)

    def enviar_cadastro(self):
        
        livro = self.livro_var.get()
        data_emprestimo = self.data_emprestimo_var.get()
        data_devolucao = self.data_devolucao_var.get()
        self.controller = EmprestimoController()
        self.controller.cadastrar_emprestimo(livro, data_emprestimo, data_devolucao)