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
        self._configurar_tela()

    def _configurar_tela(self):
        self.root.title("Lista de Empréstimos")
        self.root.attributes('-fullscreen', True)

        if self.frame:
            self.frame.destroy()

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        if self.usuario['tipo'] == 'funcionario':
            btn_cadastrar_livro = ttk.Button(self.frame, text="Cadastrar Livro", command=self.abrir_cadastro_livro)
            btn_cadastrar_livro.pack(pady=5)

        titulo = ttk.Label(self.frame, text="Empréstimos", font=("Helvetica", 16))
        titulo.pack(pady=10)

        self.tabela = ttk.Treeview(
            self.frame,
            columns=("titulo", "nome","data_emprestimo", "data_devolucao"),
            show="headings"
        )
        for col in ("titulo", "nome", "data_emprestimo", "data_devolucao"):
            self.tabela.heading(col, text=col.capitalize())
        self.tabela.pack(fill=tk.BOTH, expand=True)
        

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.voltar)
        btn_voltar.pack(pady=10)

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
