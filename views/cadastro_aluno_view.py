import tkinter as tk
from tkinter import ttk

class CadastroAlunoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame_principal = None
        self._configurar_estilos()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure('TFrame', background='white')
        style.configure('Card.TFrame',
                        background='white',
                        borderwidth=2,
                        relief='groove')
        style.configure('TLabel',
                        background='white',
                        font=('Helvetica', 12))
        style.configure('TEntry',
                        font=('Helvetica', 12))
        style.configure('TButton',
                        font=('Helvetica', 12),
                        padding=8,
                        background="#007ACC",
                        foreground="white")
        style.map('TButton',
                  background=[('active', '#005F99')],
                  foreground=[('active', 'white')])

    def mostrar(self):
        self._configurar_janela()
        self._criar_formulario()

        self.root.withdraw()
        self.root.update_idletasks()

        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.root.after(10, self._forcar_exibicao)

    def _forcar_exibicao(self):
        self.root.lift()
        self.root.focus_force()
        self.root.grab_set()

    def _configurar_janela(self):
        self.root.title("Cadastro de Aluno")
        self.root.configure(bg='#f0f0f0')
        self.root.attributes('-fullscreen', True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _criar_formulario(self):
        if self.frame_principal:
            self.frame_principal.destroy()

        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.grid(row=0, column=0, sticky='nsew')

        frame_card = ttk.Frame(self.frame_principal, style='Card.TFrame', padding=30)
        frame_card.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(frame_card, text="Cadastro de Aluno",
                  font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        # Nome
        ttk.Label(frame_card, text="Nome:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(frame_card, textvariable=self.nome_var, width=30).grid(row=1, column=1, sticky='w', padx=5, pady=5)

        # Email
        ttk.Label(frame_card, text="Email:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(frame_card, textvariable=self.email_var, width=30).grid(row=2, column=1, sticky='w', padx=5, pady=5)

        # Senha
        ttk.Label(frame_card, text="Senha:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(frame_card, textvariable=self.senha_var, width=30, show="*").grid(row=3, column=1, sticky='w', padx=5, pady=5)

        # Botões
        frame_botoes = ttk.Frame(frame_card, style="TFrame")
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        ttk.Button(frame_botoes, text="Cadastrar", command=self._cadastrar).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes, text="Voltar", command=self._voltar).pack(side=tk.LEFT, padx=10)

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
