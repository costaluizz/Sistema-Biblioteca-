import tkinter as tk
from tkinter import ttk
from controllers.emprestimo_controller import EmprestimoController
from views.menu_principal_view import MenuPrincipalView
from views.cadastro_livro_view import CadastroLivroView

class ListarEmprestimosView:
    def __init__(self, root, usuario_logado):
        self.root = root
        self.usuario = usuario_logado 
        self.controller = EmprestimoController()
        self.frame = None
        self._estilizar_interface()
        self._configurar_tela()

    def _estilizar_interface(self):
        style = ttk.Style()
        style.theme_use("clam")  # Pode usar 'clam', 'alt', 'default' ou outro disponível

        # Estilização dos botões
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=10,
                        relief="raised",
                        foreground="white",
                        background="#007ACC")
        style.map("TButton",
                  background=[('active', '#005F99'), ('disabled', '#CCCCCC')])

        # Estilização dos títulos
        style.configure("TLabel",
                        font=("Helvetica", 12),
                        padding=5)

        # Estilização da Treeview
        style.configure("Treeview",
                        font=("Helvetica", 11),
                        rowheight=30,
                        background="#F5F5F5",
                        fieldbackground="#F5F5F5")
        style.configure("Treeview.Heading",
                        font=("Helvetica", 12, "bold"),
                        background="#007ACC",
                        foreground="white")

        style.map("Treeview",
                  background=[('selected', '#CCE5FF')],
                  foreground=[('selected', 'black')])

    def _configurar_tela(self):
        self.root.title("Lista de Empréstimos")
        self.root.attributes('-fullscreen', True)

        if self.frame:
            self.frame.destroy()

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

       # if self.usuario['tipo'] == 'funcionario':
        #    btn_cadastrar_livro = ttk.Button(self.frame, text="Cadastrar Livro", command=self.abrir_cadastro_livro)
         #   btn_cadastrar_livro.pack(pady=5)

        titulo = ttk.Label(self.frame, text="Empréstimos", font=("Helvetica", 20, "bold"))
        titulo.pack(pady=20)

        self.tabela = ttk.Treeview(
            self.frame,
            columns=("titulo", "nome", "data_emprestimo", "data_devolucao"),
            show="headings"
        )
        for col in ("titulo", "nome", "data_emprestimo", "data_devolucao"):
            self.tabela.heading(col, text=col.capitalize())
            self.tabela.column(col, anchor=tk.CENTER, stretch=True)

        self.tabela.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar para a tabela
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        btn_voltar = ttk.Button(self.frame, text="Sair", command=self.root.quit)
        btn_voltar.pack(pady=15)

        self.carregar_dados()

    def carregar_dados(self):
        tipo = self.usuario['tipo']
        id_aluno = self.usuario.get('id_aluno')
        emprestimos = self.controller.listar_por_usuario(tipo, id_aluno)

        for emp in emprestimos:
            self.tabela.insert("", "end", values=(
                emp['titulo'], emp['nome'], emp['data_emprestimo'], emp['data_devolucao']
            ))

    def abrir_cadastro_livro(self):
        from views.cadastro_livro_view import CadastroLivroView
        self.frame.destroy()
        CadastroLivroView(self.root, self.usuario)

    def voltar(self):
        from views.menu_principal_view import MenuPrincipalView
        self.frame.destroy()
        self.root.deiconify()
        MenuPrincipalView(self.root, self.usuario).mostrar()
