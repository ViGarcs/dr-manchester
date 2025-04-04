# ===== BIBLIOTECAS =====
import sqlite3

# ===== FUNÇÕES DE INTERAÇÃO COM A LISTA DE USUARIOS COM CONVERSAS EM ABERTO =====

def Abrir_Conversas_Iniciadas(docs_path): # Verifica a lista de usuários com uma conversa já iniciada com o bot
    # Conectar ao banco de dados
    conn = sqlite3.connect(docs_path[0])
    cursor = conn.cursor()
    
    # Criar a tabela, se ainda não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL,
        categoria TEXT
    );
    """)
    
    # Buscar todos os registros da tabela usuarios
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()  # Retorna uma lista de tuplas
    
    # Fechar a conexão
    conn.close()
    return dados

def Inclui_Usuario_Conver_Ini(id_usuario, docs_path): # Adiciona o id dos usuários na lista de Conversas Iniciadas
    # Conectar ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect(docs_path[0])
    cursor = conn.cursor()

    # Criar a tabela, se ainda não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL,
        categoria TEXT
    );
    """)

    cursor.execute('''
    INSERT INTO usuarios (id) VALUES (?)
    ''', (id_usuario,))
    
    # Salvar e fechar
    conn.commit()
    conn.close()

def Excluir_Usuario_Conver_Ini(id_usuario, docs_path):
    # Conectar ao banco de dados
    conn = sqlite3.connect(docs_path[0])
    cursor = conn.cursor()
    
    # Executar a exclusão
    cursor.execute('''
    DELETE FROM usuarios WHERE id = ?
    ''', (id_usuario,))
    
    # Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

def Incluir_Categoria_Sintoma(id_usuario, docs_path, categoria):
    # Conectar (ou criar) o banco de dados
    conn = sqlite3.connect(docs_path[0])
    cursor = conn.cursor()
    
    # Criar a tabela usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL,
        categoria TEXT
    )
    ''')
    
    # Inserir dois registros de exemplo
    cursor.execute('''
    UPDATE usuarios SET categoria = ? WHERE id = ?
    ''', (categoria, id_usuario))
    
    # Salvar e fechar
    conn.commit()
    conn.close()
    
    