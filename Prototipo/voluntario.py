import uuid
from buscadorDeProjetos import BuscadorDeProjetos

class Voluntario: 
    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados
        self.palavras_chave = None  # Inicializa o atributo palavras_chave

    def cadastrar(self, nome_usuario, email, palavras_chave):
        dados = self.manipulador_dados.carregar_dados()
        id_voluntario = str(uuid.uuid4())
        novo_voluntario = {
            "id": id_voluntario,
            "nome_usuario": nome_usuario,
            "email": email,
            "palavras_chave": palavras_chave
        }
        dados['voluntarios'].append(novo_voluntario)
        self.manipulador_dados.salvar_dados(dados)
        return novo_voluntario 
    
    def buscar_projetos(self):
        buscador = BuscadorDeProjetos(self.manipulador_dados)
        return buscador.buscar_por_palavras_chaves(self.palavras_chave)