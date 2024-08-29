import uuid
class Voluntario: 
    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados

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