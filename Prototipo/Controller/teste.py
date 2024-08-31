import os
from historico import ManipuladorDeDados
from ong_diretor import Diretor
from voluntario import Voluntario
from projeto import Projeto
import json

def testar_funcionalidades_basicas():
    caminho_arquivo_teste = 'data_test.json'
    
    # 1. Inicializar o manipulador de dados
    manipulador_dados = ManipuladorDeDados(caminho_arquivo_teste)

    # 2. Cadastrar um diretor e seus projetos
    lista_de_projetos = [
        {"titulo": "Projeto A", "descricao": "Descrição do Projeto A", "palavras_chave": ["educação"]},
        {"titulo": "Projeto B", "descricao": "Descrição do Projeto B", "palavras_chave": ["saúde"]}
    ]
    diretor = Diretor(manipulador_dados)
    novo_diretor = diretor.cadastrar("Diretor Teste", "diretor_teste@example.com", lista_de_projetos)

    # 3. Verificar se o diretor foi cadastrado corretamente
    print("Diretor cadastrado:", novo_diretor)

    # 4. Cadastrar um voluntário
    voluntario = Voluntario(manipulador_dados)
    novo_voluntario = voluntario.cadastrar("Voluntário Teste", "voluntario_teste@example.com", ["educação", "meio ambiente"])
    
    # 5. Verificar se o voluntário foi cadastrado corretamente
    print("Voluntário cadastrado:", novo_voluntario)

    # 6. Buscar projetos com base nas palavras-chave do voluntário
    projetos_encontrados = voluntario.buscar_projetos()
    print("Projetos encontrados para o voluntário:", projetos_encontrados)

    # Limpar o arquivo de teste após o teste
    os.remove(caminho_arquivo_teste)

if __name__ == "__main__":
    testar_funcionalidades_basicas()