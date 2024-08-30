import uuid

class Diretor:
    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados

    def cadastrar(self, nome, email):
        dados = self.manipulador_dados.carregar_dados()
        id_organizador = str(uuid.uuid4())
        novo_organizador = {
            "id": id_organizador,
            "nome": nome,
            "email": email,
            "projetos": []
        }
        dados['organizadores'].append(novo_organizador)
        self.manipulador_dados.salvar_dados(dados)
        return novo_organizador
