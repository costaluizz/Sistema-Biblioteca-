import tkinter as tk

class CadastroAlunoView:
    def _init_(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)

        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()

    def mostrar(self):
        self.root.title("Cadastro de Aluno")
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Nome:").pack()
        tk.Entry(self.frame, textvariable=self.nome_var).pack(pady=5)

        tk.Label(self.frame, text="Email:").pack()
        tk.Entry(self.frame, textvariable=self.email_var).pack(pady=5)

        tk.Label(self.frame, text="Senha:").pack()
        tk.Entry(self.frame, textvariable=self.senha_var, show="*").pack(pady=5)

        tk.Button(self.frame, text="Cadastrar", command=self.enviar_cadastro).pack(pady=10)

    def enviar_cadastro(self):
        nome = self.nome_var.get()
        email = self.email_var.get()
        senha = self.senha_var.get()

        self.controller.cadastrar(nome, email, senha)