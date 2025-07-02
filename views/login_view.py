import tkinter as tk
from tkinter import ttk

class LoginView:
    def __init__(self, root, controller):  # Agora recebe 2 parâmetros
        self.root = root
        self.controller = controller
        self.frame = None
        
        # Variáveis para os campos
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.tipo_var = tk.StringVar(value="aluno")  # Valor padrão
        
        self._configurar_estilos()
    
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=5)
    
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
            
        self.frame = ttk.Frame(self.root, padding=50)
        self.frame.grid(row=0, column=0, sticky='nsew')
        
        ttk.Label(self.frame, 
                 text="Login - Sistema Biblioteca",
                 font=('Arial', 18, 'bold')).pack(pady=(0, 30))
        
        # Campos do formulário
        ttk.Label(self.frame, text="E-mail:").pack()
        ttk.Entry(self.frame, textvariable=self.email_var, width=30).pack(pady=5)
        
        ttk.Label(self.frame, text="Senha:").pack()
        ttk.Entry(self.frame, textvariable=self.senha_var, show="*", width=30).pack(pady=5)
        
        # Radio buttons para tipo de usuário
        tipo_frame = ttk.Frame(self.frame)
        tipo_frame.pack(pady=10)
        
        ttk.Label(tipo_frame, text="Tipo de usuário:").pack()
        ttk.Radiobutton(tipo_frame, text="Aluno", variable=self.tipo_var, value="aluno").pack()
        ttk.Radiobutton(tipo_frame, text="Funcionário", variable=self.tipo_var, value="funcionario").pack()
        
        # Botões
        botoes_frame = ttk.Frame(self.frame)
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