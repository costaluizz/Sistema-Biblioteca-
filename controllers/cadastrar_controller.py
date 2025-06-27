from models.cadastrar_models import Cadastrar

class CadastrarController:
    def cadastrar(self, nome, email, senha, tipo):
        cadastrar = Cadastrar(nome, email, senha, tipo)
        cadastrar.salvar()
        return cadastrar
    
    
    def listar(self):
        return Cadastrar.buscar_todos()

    