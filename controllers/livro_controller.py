from models.livro_model import Livro

class LivroController:
    def cadastrar_livro(self, titulo, autor, editora, ano):
        livro = Livro(titulo, autor, editora, ano)
        livro.salvar_livro()
        return livro

    def excluir_livro(self, livro_id):
        livro = Livro.buscar_por_id(livro_id)
        if livro:
            livro.deletar()
            return True
        return False

    def listar_livros(self):
        return Livro.buscar_todos()

    def atualizar_livro(self, titulo, autor, editora, ano,id):
        livro = Livro(titulo, autor, editora, ano,id)
        livro.salvar_livro()
        return livro