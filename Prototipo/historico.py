import json
import uuid

class ManipuladorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def carregar_dados(self):
        with open(self.caminho_arquivo, 'r') as arquivo:
            return json.load(arquivo)

    def salvar_dados(self, dados):
        with open(self.caminho_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)