from models.funcionario_model import Funcionario

class FuncionarioController:
    def cadastrar_funcionario(self, nome, email, senha):
        funcionario = Funcionario(nome, email, senha)
        funcionario.salvar_funcionario()
        return funcionario

    def excluir_funcionario(self, funcionario_id):
        funcionario = Funcionario.buscar_por_id(funcionario_id)
        if funcionario:
            funcionario.deletar()
            return True
        return False

    def listar_funcionarios(self):
        return Funcionario.buscar_todos()

    def atualizar_funcionario(self, nome, email, senha, id):
        funcionario = Funcionario(nome, email, senha, id)
        funcionario.salvar_funcionario()
        return funcionario