class BuscadorDeProjetos:

    def __init__(self, manipulador_dados):
        self.manipulador_dados = manipulador_dados
        #self.dados = self.manipulador_dados.carregar_dados()

    def buscar_por_palavras_chaves(self, palavras_chave_voluntario):
        # Recuperar a lista de todos os projetos
        todos_projetos = []
        for organizador in self.dados['organizadores']:
            todos_projetos.extend(organizador['projetos'])

        # Filtrar os projetos com base nas palavras-chave do voluntário
        projetos_correspondentes = [
            projeto for projeto in todos_projetos
            if any(keyword in projeto['palavras_chave'] for keyword in palavras_chave_voluntario)
        ]
        
        return projetos_correspondentes