# ===== BIBLIOTECAS =====
# -- BIBLIOTECAS EXTERNAS --
import sqlite3

# -- MÓDULOS INTERNOS DO PROJETO --
from Funcoes_Conversas_Iniciadas import Incluir_Categoria_Sintoma
from Funcoes_Conversas_Iniciadas import Inclui_Usuario_Conver_Ini

# ===== FUNÇÕES LÓGICAS: APOIAM AS FUNÇÕES DE COMUNICAÇÃO COM O TELEGRAM =====

def Verificar_Codigo_Usuario(docs_path, codigo):
    conn = sqlite3.connect(docs_path[0])
    cursor = conn.cursor()
    
    # Criar a tabela, se ainda não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL,
        categoria TEXT
    );
    """)
    
    # Consulta para verificar se o id existe
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id = ?", (codigo,))
    resultado = cursor.fetchone()[0]  # Retorna o número de ocorrências

    conn.close()
    return resultado > 0  # Retorna True se existe, False se não


def Verifica_Funcao_Pos_Categoria(mensagem, docs_path): # Verifica se o usuário já informou a categoria do caso
    categorias = ["/Alergia", "/Asma", "/Autoagressao", "/Bebe_Chorando", "/Cefaleia", "/Convulsoes", "/Desmaio", "/Diarreia_e_ou_vomitos", "/Dispneia_em_adulto", "/Dispneia_em_crianca", "/Dor_abdominal_em_adulto", "/Dor_abdominal_em_crianca", "/Dor_de_garganta", "/Dor_lombar", "/Dor_toracica", "/Mal_estar_em_adulto", "/Pais_preocupados", "/Quedas", "/Trauma_cranioencefalico", "/Trauma_maior"]
    conversa_iniciada = Verificar_Codigo_Usuario(docs_path, mensagem.chat.id)
    
    if conversa_iniciada:
        if mensagem.text in categorias:
            if mensagem.text == "/Diarreia_e_ou_vomitos":
                categoria = "Diarreia e/ou vomitos"
            else:
                categoria = mensagem.text[1:].replace("_", " ")
            Incluir_Categoria_Sintoma(mensagem.chat.id, docs_path, categoria)
            return True
        
        else:
            return False
    else:
        return False


def Verificar_Mensagem_Pos_Sintomas(mensagem, docs_path): # Verifica se o usuário já informou os sintomas
    categorias = ["/Alergia", "/Asma", "/Autoagressao", "/Bebe_Chorando", "/Cefaleia", "/Convulsoes", "/Desmaio", "/Diarreia_e_ou_vomitos", "/Dispneia_em_adulto", "/Dispneia_em_crianca", "/Dor_abdominal_em_adulto", "/Dor_abdominal_em_crianca", "/Dor_de_garganta", "/Dor_lombar", "/Dor_toracica", "/Mal_estar_em_adulto", "/Pais_preocupados", "/Quedas", "/Trauma_cranioencefalico", "/Trauma_maior"]
    conversa_iniciada = Verificar_Codigo_Usuario(docs_path, mensagem.chat.id)
    
    if conversa_iniciada:
        # Verifica o banco de dados para checar se a coluna de categorias ja foi preenchida,
        # caso não tenha sido preenchida, ele não deve pular para essa etapa ainda
        conn = sqlite3.connect(docs_path[0])
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM usuarios WHERE id = ? AND categoria IS NOT NULL", (mensagem.chat.id,))
        resultado = cursor.fetchone() is not None  # Armazena True ou False
        
        conn.close()
        
        if mensagem.text in categorias or not resultado:
            return False
        
        else:
            return True
        
    else:
        return False


def Verificar_Mensagem_Inicial(mensagem, docs_path): # Verifica se o usuário já tem alguma conversa em aberto ou se é a primeira interação
    conversa_iniciada = Verificar_Codigo_Usuario(docs_path, mensagem.chat.id)
    
    if not conversa_iniciada:
        Inclui_Usuario_Conver_Ini(mensagem.chat.id, docs_path)
        return True
        
    else:
        return False



