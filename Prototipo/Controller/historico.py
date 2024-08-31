import json
import uuid

class ManipuladorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            # Inicializa a estrutura de dados se o arquivo não existir
            return {
                "voluntarios": [],
                "organizadores": [],
                "projetos": []
            }

    def salvar_dados(self, dados):
        with open(self.caminho_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    def obter_dados(self):
        return self.dados
    
    def atualizar_dados(self, novos_dados):
        self.dados = novos_dados
        self.salvar_dados(self.dados)  # Corrigir para passar self.dados como argumento
