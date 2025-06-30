import tkinter as tk

class LoginView:

    def __init__(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)

        self.root.attributes('-fullscreen', True)
    def mostrar(self):
        self.root.title("Tela de Login")
        self.frame.pack(padx=20, pady=20)
        var_opcao = tk.StringVar(value="")

        tk.Label(self.root, text = "E-mail:").pack(pady=8)
        entry_email = tk.Entry(self.root, width=25)
        entry_email.pack(pady=5)

        tk.Label(self.root, text = "Senha:").pack(pady=8)
        entry_senha = tk.Entry(self.root, show="*", width=25)
        entry_senha.pack(pady=10)

        tk.Label(self.root, text = "Escolha uma opção:").pack(pady=10)

        tk.Radiobutton(self.root, text="Aluno", variable=var_opcao, value="aluno").pack()
        tk.Radiobutton(self.root, text="Funcionário", variable=var_opcao, value="funcionario").pack()