import sqlite3
import os

# Função para inicializar o banco de dados
def init_db():
    # Verifica se o arquivo database.db já existe e remove se estiver corrompido
    if os.path.exists('database.db'):
        print("Arquivo 'database.db' já existe. Excluindo...")
        os.remove('database.db')  # Remove o arquivo se ele já existir

    # Conecta ou cria o banco de dados 'database.db'
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Criação da tabela 'usuarios' com tipo_usuario como INTEGER
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            numero_identificacao TEXT PRIMARY KEY,
            tipo_usuario INTEGER NOT NULL,  -- 1 para Estudante, 2 para Funcionário
            pontos INTEGER DEFAULT 0
        )
    ''')

    # Criação da tabela 'doacoes'
    c.execute('''
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id TEXT,
            categoria TEXT NOT NULL,
            item TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data_doacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            pontos INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(numero_identificacao)
        )
    ''')

    conn.commit()  # Salva as mudanças
    conn.close()   # Fecha a conexão

# Executa a função para criar as tabelas
if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso!")
