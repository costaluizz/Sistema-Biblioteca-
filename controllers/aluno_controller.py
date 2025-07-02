from models.aluno_model import Aluno

class AlunoController:
    def cadastrar_aluno(self,nome,email,senha):
        aluno = Aluno(nome, email, senha)
        aluno.salvar_aluno()
        return aluno
    
    def excluir_aluno(self, id_aluno):
        aluno = Aluno.buscar_por_id(id_aluno)
        if aluno:
            aluno.deletar()
            return True
        return False
    
    def listar_alunos(self):
        return Aluno.buscar_todos()
    
    def atualizar_aluno(self,nome,email,senha,id):
        aluno = Aluno(nome, email, senha, id)
        aluno.salvar_aluno()
        return aluno
    
