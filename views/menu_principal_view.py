import tkinter as tk
from tkinter import ttk

class MenuPrincipalView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None
        self._configurar_estilos()
        
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        
    def mostrar(self):
        self._configurar_janela()
        self._criar_widgets()
        
    def _configurar_janela(self):
        self.root.title(f"Menu Principal - {self.controller.tipo_usuario.capitalize()}")
        self.root.configure(bg='#f0f0f0')
        self.root.attributes('-fullscreen', True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_widgets(self):
        if self.frame:
            self.frame.destroy()
            
        self.frame = ttk.Frame(self.root, padding=50)
        self.frame.grid(row=0, column=0, sticky='nsew')
        
        ttk.Label(self.frame, 
                 text=f"Bem-vindo ao Sistema\n({self.controller.tipo_usuario})",
                 font=('Arial', 18, 'bold'),
                 justify='center').pack(pady=(0, 30))
        
        # Frame dos botões
        botoes_frame = ttk.Frame(self.frame)
        botoes_frame.pack(pady=20)
        
        # Botões com base no tipo de usuário
        if self.controller.tipo_usuario == 'funcionario':
            botoes = [
                ("Cadastrar Alunos", self.controller.abrir_cadastro_alunos),
                ("Cadastrar Livros", self.controller.abrir_cadastro_livros),
                ("Gerenciar Empréstimos", self.controller.abrir_emprestimos)
            ]
        else:  # Aluno
            botoes = [
                ("Solicitar Empréstimo", self.controller.abrir_emprestimos),
                ("Meus Empréstimos", self.controller.abrir_emprestimos)
            ]
        
        for texto, comando in botoes:
            btn = ttk.Button(
                botoes_frame,
                text=texto,
                command=comando,
                width=25
            )
            btn.pack(pady=10, ipady=10)
        
        ttk.Button(
            self.frame,
            text="Sair",
            command=self.controller.sair,
            style='danger.TButton'
        ).pack(side=tk.BOTTOM, pady=20)