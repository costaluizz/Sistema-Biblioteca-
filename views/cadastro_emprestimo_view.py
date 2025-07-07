import tkinter as tk
from tkinter import ttk
from controllers.emprestimo_controller import EmprestimoController

class CadastroEmprestimoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root, bg="#f0f0f0")  # Cor de fundo clara

        self.livro_var = tk.StringVar()
        self.data_emprestimo_var = tk.StringVar()
        self.data_devolucao_var = tk.StringVar()

        self._estilizar()

    def _estilizar(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), padding=8,
                        background="#007ACC", foreground="white")
        style.map("TButton",
                  background=[('active', '#005F99')],
                  foreground=[('active', 'white')])

    def mostrar(self):
        self.root.title("Cadastro de Empréstimo")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Campo Livro
        campo1 = ttk.Frame(self.frame, padding=5, style='TFrame')
        campo1.pack(fill="x", pady=5)
        ttk.Label(campo1, text="Livro:").pack(anchor='w')
        ttk.Entry(campo1, textvariable=self.livro_var, width=40).pack()

        # Campo Data de Empréstimo
        campo2 = ttk.Frame(self.frame, padding=5, style='TFrame')
        campo2.pack(fill="x", pady=5)
        ttk.Label(campo2, text="Data de Empréstimo:").pack(anchor='w')
        ttk.Entry(campo2, textvariable=self.data_emprestimo_var, width=40).pack()

        # Campo Data de Devolução
        campo3 = ttk.Frame(self.frame, padding=5, style='TFrame')
        campo3.pack(fill="x", pady=5)
        ttk.Label(campo3, text="Data de Devolução:").pack(anchor='w')
        ttk.Entry(campo3, textvariable=self.data_devolucao_var, width=40).pack()

        # Botão Cadastrar
        ttk.Button(self.frame, text="Cadastrar", command=self.enviar_cadastro).pack(pady=15)

    def enviar_cadastro(self):
        livro = self.livro_var.get()
        data_emprestimo = self.data_emprestimo_var.get()
        data_devolucao = self.data_devolucao_var.get()
        self.controller = EmprestimoController()
        self.controller.cadastrar_emprestimo(livro, data_emprestimo, data_devolucao)
