import tkinter as tk
from tkinter import ttk

class CadastroAlunoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame_principal = None
        self._configurar_estilos()
        
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame',  background='white')
        self.style.configure('TLabel', background='white', font=('Arial', 12))
        self.style.configure('TButton', background='white', font=('Arial', 12), padding=5)
        self.style.configure('TEntry', font=('Arial', 12), padding=5)
        self.style.configure('Card.TFrame', background='white', borderwidth=2, relief='groove')

    def mostrar(self):
        """Exibe a janela de cadastro garantindo que ficará visível imediatamente"""
        self._configurar_janela()
        self._criar_formulario()
        
        # Configurações extras para garantir visibilidade
        self.root.withdraw()  # Esconde temporariamente
        self.root.update_idletasks()  # Processa todas as operações pendentes
        
        # Centraliza a janela (opcional)
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')
        
        # Garante que a janela apareça corretamente
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        
        # Solução definitiva para o bug do Alt+Tab
        self.root.after(10, self._forcar_exibicao)

    def _forcar_exibicao(self):
        """Método auxiliar para garantir a exibição"""
        self.root.lift()
        self.root.focus_force()
        self.root.grab_set()  # Garante que a janela mantenha o foco
            
    def _configurar_janela(self):
        self.root.title("Cadastro de Aluno")
        self.root.configure(bg='#f0f0f0')
        self.root.attributes('-fullscreen', True)
        
        # Configuração para centralização
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_formulario(self):
        # Limpa o frame anterior se existir
        if self.frame_principal:
            self.frame_principal.destroy()
            
        # Frame principal que ocupa toda a janela
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.grid(row=0, column=0, sticky='nsew')
        
        # Frame do cartão (formulário) - centralizado
        frame_card = ttk.Frame(self.frame_principal, style='Card.TFrame', padding=30)
        frame_card.place(relx=0.5, rely=0.5, anchor='center')
        
        # Título
        lbl_titulo = ttk.Label(frame_card, 
                             text="Cadastro de Aluno",
                             font=('Arial', 16, 'bold'))
        lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Variáveis para os campos
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        
        # Campos do formulário
        lbl_nome = ttk.Label(frame_card, text="Nome:")
        lbl_nome.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        
        entry_nome = ttk.Entry(frame_card, textvariable=self.nome_var, width=30)
        entry_nome.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        lbl_email = ttk.Label(frame_card, text="Email:")
        lbl_email.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        
        entry_email = ttk.Entry(frame_card, textvariable=self.email_var, width=30)
        entry_email.grid(row=2, column=1, sticky='w', padx=5, pady=5)
        
        lbl_senha = ttk.Label(frame_card, text="Senha:")
        lbl_senha.grid(row=3, column=0, sticky='e', padx=5, pady=5)
        
        entry_senha = ttk.Entry(frame_card, textvariable=self.senha_var, width=30, show="*")
        entry_senha.grid(row=3, column=1, sticky='w', padx=5, pady=5)
        
        # Frame dos botões
        frame_botoes = ttk.Frame(frame_card)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=(20, 0))
        
        btn_cadastrar = ttk.Button(frame_botoes, 
                                 text="Cadastrar", 
                                 command=self._cadastrar)
        btn_cadastrar.pack(side=tk.LEFT, padx=10)
        
        btn_voltar = ttk.Button(frame_botoes, 
                              text="Voltar", 
                              command=self._voltar)
        btn_voltar.pack(side=tk.LEFT, padx=10)
    
    def _cadastrar(self):
        nome = self.nome_var.get()
        email = self.email_var.get()
        senha = self.senha_var.get()
        
        if self.controller.cadastrar(nome, email, senha):
            self.limpar_campos()
    
    def _voltar(self):
        from controllers.login_controller import LoginController
        self.frame_principal.destroy()
        LoginController(self.root).iniciar_login()
    
    def limpar_campos(self):
        self.nome_var.set("")
        self.email_var.set("")
        self.senha_var.set("")