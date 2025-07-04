import tkinter as tk
from controllers.livro_controller import LivroController


class CadastroLivroView:
    def __init__(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)

        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.ano_var = tk.StringVar()
        self.editora_var = tk.StringVar()

    def mostrar(self):
        self.root.title("Cadastro de Livro")
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Título:").pack()
        tk.Entry(self.frame, textvariable=self.titulo_var).pack(pady=5)

        tk.Label(self.frame, text="Autor:").pack()
        tk.Entry(self.frame, textvariable=self.autor_var).pack(pady=5)

        tk.Label(self.frame, text="Ano de Publicação:").pack()
        tk.Entry(self.frame, textvariable=self.ano_var).pack(pady=5)

        tk.Label(self.frame, text="Editora:").pack()
        tk.Entry(self.frame, textvariable=self.editora_var).pack(pady=5)

        tk.Button(self.frame, text="Cadastrar", command=self.enviar_cadastro).pack(pady=10)

    def enviar_cadastro(self):
        titulo = self.titulo_var.get()
        autor = self.autor_var.get()
        ano = self.ano_var.get()
        editora = self.editora_var.get()
        self.controller = LivroController()
        self.controller.cadastrar_livro(titulo, autor, ano, editora)   

