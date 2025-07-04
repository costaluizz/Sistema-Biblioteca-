import tkinter as tk
from tkinter import ttk, messagebox
from controllers.livro_controller import LivroController

class CadastroLivroView:
    def __init__(self, root, usuario):
        self.root = root  
        self.usuario = usuario
        self.controller = LivroController()
        self.frame_principal = None

        self._configurar_estilos()
        self._configurar_janela()
        self._criar_formulario()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='white')
        self.style.configure('TLabel', background='white', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=5)

    def _configurar_janela(self):
        self.root.title("Cadastro de Livro")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='white')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _criar_formulario(self):
        if self.frame_principal:
            self.frame_principal.destroy()

        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.grid(row=0, column=0, sticky='nsew')

        form_frame = ttk.Frame(self.frame_principal, padding=30, style='TFrame')
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(form_frame, text="Cadastro de Livro", font=('Arial', 16, 'bold')).grid(columnspan=2, pady=(0, 20))

        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.editora_var = tk.StringVar()
        self.ano_var = tk.StringVar()

        campos = [("Título", self.titulo_var), ("Autor", self.autor_var), ("Editora", self.editora_var), ("Ano", self.ano_var)]

        for i, (label, var) in enumerate(campos):
            ttk.Label(form_frame, text=label + ":").grid(row=i, column=0, sticky='e', padx=10, pady=5)
            ttk.Entry(form_frame, textvariable=var, width=30).grid(row=i, column=1, sticky='w', padx=10, pady=5)

        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Cadastrar", command=self._cadastrar).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Voltar", command=self._voltar).pack(side=tk.LEFT, padx=10)

    def _cadastrar(self):
        titulo = self.titulo_var.get()
        autor = self.autor_var.get()
        editora = self.editora_var.get()
        ano = self.ano_var.get()

        if not (titulo and autor and editora and ano):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        self.controller.cadastrar_livro(titulo, autor, editora, ano)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        self._limpar_campos()

    def _voltar(self):
        from views.menu_principal_view import MenuPrincipalView
        self.frame_principal.destroy()
        MenuPrincipalView(self.root, self.usuario).mostrar()

    def _limpar_campos(self):
        self.titulo_var.set("")
        self.autor_var.set("")
        self.editora_var.set("")
        self.ano_var.set("")