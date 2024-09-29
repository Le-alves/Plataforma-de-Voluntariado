import sqlite3

# Função para verificar as doações de um usuário
def verificar_doacoes(numero_identificacao):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Consulta para buscar as doações do usuário
    c.execute('SELECT id, categoria, item, quantidade, pontos, data_doacao FROM doacoes WHERE usuario_id = ?', (numero_identificacao,))
    doacoes = c.fetchall()

    conn.close()

    # Se não houver doações, retorna uma mensagem
    if not doacoes:
        return f"Usuário {numero_identificacao} não fez nenhuma doação."
    
    # Exibe todas as doações encontradas
    resultado = f"Doações do usuário {numero_identificacao}:\n"
    for doacao in doacoes:
        resultado += f"- ID: {doacao[0]}, Categoria: {doacao[1]}, Item: {doacao[2]}, Quantidade: {doacao[3]}, Pontos: {doacao[4]}, Data: {doacao[5]}\n"
    
    return resultado

# Exemplo de uso
if __name__ == '__main__':
    numero_identificacao = input("Digite o número de identificação (matrícula ou registro) para verificar doações: ")
    
    # Verificar doações do usuário
    resultado = verificar_doacoes(numero_identificacao)
    print(resultado)
