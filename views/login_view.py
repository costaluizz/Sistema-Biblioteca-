import tkinter as tk
from tkinter import ttk

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None

        # Variáveis dos campos
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.tipo_var = tk.StringVar(value="aluno")

        self._configurar_estilos()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 14))
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.configure('TRadiobutton', background='#f0f0f0', font=('Arial', 12))

    def mostrar(self):
        self._configurar_janela()
        self._criar_formulario()

    def _configurar_janela(self):
        self.root.title("Login - Sistema Biblioteca")
        self.root.configure(bg='#f0f0f0')
        self.root.attributes('-fullscreen', True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _criar_formulario(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ttk.Frame(self.root, padding=40)
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        container = ttk.Frame(self.frame)
        container.pack(expand=True)

        ttk.Label(container,
                  text="Login - Sistema Biblioteca",
                  font=('Arial', 20, 'bold')).pack(pady=(0, 30))

        ttk.Label(container, text="E-mail:").pack(anchor='w')
        ttk.Entry(container, textvariable=self.email_var, width=40, font=('Arial', 12)).pack(pady=(0, 15))

        ttk.Label(container, text="Senha:").pack(anchor='w')
        ttk.Entry(container, textvariable=self.senha_var, show="*", width=40, font=('Arial', 12)).pack(pady=(0, 15))

        tipo_frame = ttk.Frame(container)
        tipo_frame.pack(pady=(10, 20), anchor='w')

        ttk.Label(tipo_frame, text="Tipo de usuário:").pack(anchor='w')
        ttk.Radiobutton(tipo_frame, text="Aluno", variable=self.tipo_var, value="aluno").pack(anchor='w')
        ttk.Radiobutton(tipo_frame, text="Funcionário", variable=self.tipo_var, value="funcionario").pack(anchor='w')

        botoes_frame = ttk.Frame(container)
        botoes_frame.pack(pady=20)

        ttk.Button(botoes_frame,
                   text="Entrar",
                   command=self.controller.verificar_login).pack(side=tk.LEFT, padx=10)

        ttk.Button(botoes_frame,
                   text="Cadastrar",
                   command=self.controller.abrir_tela_cadastro).pack(side=tk.LEFT, padx=10)

        ttk.Button(botoes_frame,
                   text="Sair",
                   command=self.controller.sair).pack(side=tk.LEFT, padx=10)
