import uuid
from projeto import Projeto
#MUDAR NOME DO ARQUIVO
class Diretor:
    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados

    def cadastrar(self, nome, email, lista_de_projetos):
        dados = self.manipulador_dados.carregar_dados()
        id_organizador = str(uuid.uuid4())
        novo_organizador = {
            "id": id_organizador,
            "nome": nome,
            "email": email,
            "projetos": []
        }
        dados['organizadores'].append(novo_organizador)

        # Instanciar a classe Projeto
        projeto_class = Projeto(self.manipulador_dados)

        # Verificar e adicionar projetos
        for projeto in lista_de_projetos:
            novo_projeto = projeto_class.criar_projeto(projeto['titulo'], projeto['descricao'], id_organizador, projeto['palavras_chave'])
            novo_organizador['projetos'].append(novo_projeto)

        # Salvar os dados atualizados
        self.manipulador_dados.atualizar_dados(dados)

        return novo_organizador
