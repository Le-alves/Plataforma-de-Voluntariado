import uuid

class Projeto: 

    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados

    def criar_projeto(self, titulo, descricao, id_organizador, palavras_chave):
        dados = self.manipulador_dados.carregar_dados()

        # Gerando um ID único para o novo projeto
        id_projeto = str(uuid.uuid4())
        
        # Criando o novo projeto como um dicionário
        novo_projeto = {
            "id": id_projeto,
            "titulo": titulo,
            "descricao": descricao,
            "id_organizador": id_organizador,
            "palavras_chave": palavras_chave
        }

        # Adicionando o projeto ao organizador correspondente
        for organizador in dados['organizadores']:
            if organizador['id'] == id_organizador:
                organizador['projetos'].append(novo_projeto)
                break

        # Adicionando o projeto à lista global de projetos
        dados['projetos'].append(novo_projeto)

        # Salvando os dados atualizados no JSON
        self.manipulador_dados.salvar_dados(dados)

        # Retornando o projeto criado
        return novo_projeto



    def obter_projeto_por_id(self, id_projeto):
        dados = self.manipulador_dados.carregar_dados()
        for projeto in dados['projetos']:
            if projeto['id'] == id_projeto:
                return projeto
        return None
