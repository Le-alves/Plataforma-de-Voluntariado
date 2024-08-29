import os
from historico import ManipuladorDeDados
from ong_diretor import Diretor
from voluntario import Voluntario
from projeto import Projeto

def testar_criacao_diretor():
    # Caminho para o arquivo JSON de teste
    caminho_arquivo_teste = 'data_test.json'
    
    # Criar um arquivo de teste com dados vazios
    with open(caminho_arquivo_teste, 'w') as f:
        f.write('{"organizadores": [], "voluntarios": [], "projetos": []}')
    
    # Instanciar o manipulador de dados
    manipulador_dados = ManipuladorDeDados(caminho_arquivo_teste)
    
    # Criar um diretor
    diretor = Diretor(manipulador_dados)
    novo_diretor = diretor.cadastrar("ONG Teste", "ong_teste@example.com")
    
    # Verificar se o diretor foi criado corretamente
    assert novo_diretor['nome'] == "ONG Teste"
    assert novo_diretor['email'] == "ong_teste@example.com"
    
    print("Teste de criação de diretor: SUCESSO")

def testar_criacao_voluntario():
    caminho_arquivo_teste = 'data_test.json'
    
    manipulador_dados = ManipuladorDeDados(caminho_arquivo_teste)
    
    # Criar um voluntário
    voluntario = Voluntario(manipulador_dados)
    novo_voluntario = voluntario.cadastrar("João", "joao@example.com", ["educação", "meio ambiente"])
    
    # Verificar se o voluntário foi criado corretamente
    assert novo_voluntario['nome_usuario'] == "João"
    assert novo_voluntario['email'] == "joao@example.com"
    
    print("Teste de criação de voluntário: SUCESSO")

def testar_criacao_projeto():
    caminho_arquivo_teste = 'data_test.json'
    
    manipulador_dados = ManipuladorDeDados(caminho_arquivo_teste)
    
    # Criar um projeto associado ao diretor criado anteriormente
    projeto = Projeto(manipulador_dados)
    novo_projeto = projeto.criar_projeto(
        "Projeto Teste", 
        "Este é um projeto de teste.", 
        id_organizador="ID_DO_DIRETOR",  # Você precisa substituir por um ID real obtido dos testes anteriores
        palavras_chave=["teste", "projeto"]
    )
    
    # Verificar se o projeto foi criado corretamente
    assert novo_projeto['titulo'] == "Projeto Teste"
    assert novo_projeto['descricao'] == "Este é um projeto de teste."
    
    print("Teste de criação de projeto: SUCESSO")

if __name__ == "__main__":
    testar_criacao_diretor()
    testar_criacao_voluntario()
    testar_criacao_projeto()
    
    # Remover o arquivo de teste após os testes
    #os.remove('data_test.json')
