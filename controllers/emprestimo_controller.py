from models.emprestimo_model import Emprestimo

class EmprestimoController:
    def cadastrar_emprestimo(self, id_livro, data_emprestimo, data_devolucao, id_aluno):
        emprestimo = Emprestimo(id_livro, data_emprestimo, data_devolucao, id_aluno)
        emprestimo.salvar_emprestimos()
        return emprestimo

    def excluir_emprestimo(self,emprestimo_id):
        emprestimo = Emprestimo.buscar_por_id(emprestimo_id)
        if emprestimo:
            emprestimo.deletar()
            return True
        return False
    
    def listar_emprestimos(self):
        return Emprestimo.buscar_todos()
    
    def atualizar_emprestimo(self, id_livro, data_emprestimo, data_devolucao, id_aluno,id):
        emprestimo = Emprestimo(id_livro,data_emprestimo,data_devolucao,id_aluno,id)
        emprestimo.salvar_emprestimos()
        return emprestimo   
        
    def listar_por_usuario(self, tipo_usuario, id_aluno=None):
        print(tipo_usuario, id_aluno)
        if tipo_usuario == 'funcionario':
            return Emprestimo.buscar_todos()
        elif tipo_usuario == 'aluno' and id_aluno:
            return Emprestimo.buscar_por_aluno(id_aluno)
        else:
            return []
