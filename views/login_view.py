import tkinter as tk
from tkinter import messagebox

class LoginView:

    def _init_(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)

        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.tipo_var = tk.StringVar(value="")

        self.root.attributes('-fullscreen', True)

    def mostrar(self):
        self.root.title("Tela de Login")
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="E-mail:").pack(pady=8)
        tk.Entry(self.frame, textvariable=self.email_var, width=25).pack()

        tk.Label(self.frame, text="Senha:").pack(pady=8)
        tk.Entry(self.frame, textvariable=self.senha_var, show="*", width=25).pack()

        tk.Label(self.frame, text="Escolha o tipo de usuário:").pack(pady=10)
        tk.Radiobutton(self.frame, text="Aluno", variable=self.tipo_var, value="aluno").pack()
        tk.Radiobutton(self.frame, text="Funcionário", variable=self.tipo_var, value="funcionario").pack()

        tk.Button(self.frame, text="Login", command=self.controller.verificar_login).pack(pady=30)
        tk.Button(self.frame, text="Cadastrar").pack(pady=40)