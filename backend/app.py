#Arquivo principal do Flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('database.db')

# Rota para registrar um novo usuário
@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    numero_identificacao = data['numero_identificacao']
    tipo_usuario = data['tipo_usuario']

    conn = connect_db()
    c = conn.cursor()

    # Verificar se o usuário já existe
    c.execute('SELECT * FROM usuarios WHERE numero_identificacao = ?', (numero_identificacao,))
    if c.fetchone():
        return jsonify({'message': 'Usuário já existe no banco de dados.'}), 400

    # Registrar o usuário
    c.execute('INSERT INTO usuarios (numero_identificacao, tipo_usuario) VALUES (?, ?)',
              (numero_identificacao, tipo_usuario))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

#Rota para consultar Usuario 
@app.route('/consultar_usuario/<numero_identificacao>', methods=['GET'])
def consultar_usuario(numero_identificacao):
    conn = connect_db()
    c = conn.cursor()

    # Buscar as informações do usuário
    c.execute('SELECT numero_identificacao, tipo_usuario FROM usuarios WHERE numero_identificacao = ?', (numero_identificacao,))
    usuario = c.fetchone()

    if not usuario:
        conn.close()
        return jsonify({'message': 'Usuário não encontrado.'}), 404

    # Calcular a soma dos pontos a partir das doações
    c.execute('SELECT SUM(pontos) FROM doacoes WHERE usuario_id = ?', (numero_identificacao,))
    pontos_totais = c.fetchone()[0]
    conn.close()

    # Se não houver doações, pontos_totais será None. Definir como 0.
    if pontos_totais is None:
        pontos_totais = 0

    # Conversão do tipo de usuário para "Estudante" ou "Funcionário"
    tipo_usuario = "Estudante" if usuario[1] == 1 else "Funcionário"

    return jsonify({
        'numero_identificacao': usuario[0],
        'tipo_usuario': tipo_usuario,
        'pontos': pontos_totais
    }), 200


#Registrar Doações
@app.route('/registrar_doacao', methods=['POST'])
def registrar_doacao():
    data = request.get_json()
    numero_identificacao = data['numero_identificacao']
    categoria = data['categoria']
    item = data['item']
    quantidade = int(data['quantidade'])
    pontos = quantidade * 10  # Controle dos pontos

    conn = connect_db()
    c = conn.cursor()

    # Verificar se o usuário existe
    c.execute('SELECT * FROM usuarios WHERE numero_identificacao = ?', (numero_identificacao,))
    if not c.fetchone():
        return jsonify({'message': 'Usuário não encontrado. Por favor, registre o usuário primeiro.'}), 400

    # Registrar a doação
    c.execute('INSERT INTO doacoes (usuario_id, categoria, item, quantidade, pontos) VALUES (?, ?, ?, ?, ?)',
              (numero_identificacao, categoria, item, quantidade, pontos))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Doação registrada com sucesso!', 'pontos': pontos}), 201

@app.route('/consultar_doacoes/<numero_identificacao>', methods=['GET'])
def consultar_doacoes(numero_identificacao):
    conn = connect_db()
    c = conn.cursor()

    # Buscar todas as doações do usuário com o numero_identificacao fornecido
    c.execute('SELECT id, categoria, item, quantidade, pontos, data_doacao FROM doacoes WHERE usuario_id = ?',
              (numero_identificacao,))
    doacoes = c.fetchall()
    conn.close()

    # Se não houver doações, retorna uma mensagem
    if not doacoes:
        return jsonify({'message': f'Nenhuma doação encontrada para o usuário {numero_identificacao}.'}), 404

    # Montar a resposta com os detalhes de cada doação
    resultado = []
    for doacao in doacoes:
        resultado.append({
            'id': doacao[0],
            'categoria': doacao[1],
            'item': doacao[2],
            'quantidade': doacao[3],
            'pontos': doacao[4],
            'data_doacao': doacao[5]
        })
    
    return jsonify({'usuario_id': numero_identificacao, 'doacoes': resultado}), 200

#Total de pontos da instituição
@app.route('/total_pontos_instituicao', methods=['GET'])
def total_pontos_instituicao():
    conn = connect_db()
    c = conn.cursor()

    # Consulta SQL para somar todos os pontos da tabela de doações
    c.execute('SELECT SUM(pontos) FROM doacoes')
    total_pontos = c.fetchone()[0]
    conn.close()

    # Se não houver doações, retorna zero como total de pontos
    if total_pontos is None:
        total_pontos = 0

    return jsonify({'total_pontos_instituicao': total_pontos}), 200

#Rota para todos os usuário 
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = connect_db()
    c = conn.cursor()

    # Buscar todos os usuários
    c.execute('SELECT numero_identificacao, tipo_usuario FROM usuarios')
    usuarios = c.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        numero_identificacao = usuario[0]

        # Calcular a soma dos pontos a partir das doações para cada usuário
        c.execute('SELECT SUM(pontos) FROM doacoes WHERE usuario_id = ?', (numero_identificacao,))
        pontos_totais = c.fetchone()[0]

        if pontos_totais is None:
            pontos_totais = 0

        # Conversão do tipo de usuário para "Estudante" ou "Funcionário"
        tipo_usuario = "Estudante" if usuario[1] == 1 else "Funcionário"

        lista_usuarios.append({
            'numero_identificacao': numero_identificacao,
            'tipo_usuario': tipo_usuario,
            'pontos': pontos_totais
        })

    conn.close()
    return jsonify({'usuarios': lista_usuarios}), 200

#Total de Doações
@app.route('/total_doacoes', methods=['GET'])
def total_doacoes():
    conn = connect_db()
    c = conn.cursor()

    # Consulta SQL para contar o total de itens doados na tabela de doações
    c.execute('SELECT SUM(quantidade) FROM doacoes')
    total_doacoes = c.fetchone()[0]
    conn.close()

    # Se não houver doações, retorna zero como total de doações
    if total_doacoes is None:
        total_doacoes = 0

    return jsonify({'total_doacoes': total_doacoes}), 200

#Histórico de todas as doações
@app.route('/historico_completo', methods=['GET'])
def historico_completo():
    conn = connect_db()
    c = conn.cursor()

    # Consulta SQL para buscar todas as doações registradas no banco de dados
    c.execute('SELECT usuario_id, categoria, item, quantidade, pontos, data_doacao FROM doacoes ORDER BY data_doacao ASC')
    historico = c.fetchall()
    conn.close()

    # Montar a resposta com os detalhes de cada doação
    historico_completo = []
    for doacao in historico:
        historico_completo.append({
            'usuario_id': doacao[0],
            'categoria': doacao[1],
            'item': doacao[2],
            'quantidade': doacao[3],
            'pontos': doacao[4],
            'data_doacao': doacao[5]
        })

    return jsonify({'historico_completo': historico_completo}), 200


# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)