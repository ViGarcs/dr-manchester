# ===== DEPENDENCIAS =====
# pip install sentence-transformers

# ===== BIBLIOTECAS =====
# -- BIBLIOTECAS EXTERNAS --
import sqlite3
from sentence_transformers import SentenceTransformer, util 

# -- MÓDULOS INTERNOS DO PROJETO --
from Funcoes_Conversas_Iniciadas import Abrir_Conversas_Iniciadas

# ===== VARIAVEIS GLOBAIS =====
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# ===== TRATAMENTO DE MENSAGENS DO USUÁRIO =====
def Importar_Banco_Protocolo_Manchester(docs_path):
    conn = sqlite3.connect(docs_path[1])
    cursor = conn.cursor()
    cursor.execute("SELECT id, categoria_clinica, sintoma_especifico, classificacao_manchester FROM sintomas_manchester")
    casos = cursor.fetchall()
    conn.close()
    
    return casos


def Filtro_Mensagens_Usuario(mensagem, docs_path):
    texto_msg = mensagem.text
    if ';' in texto_msg:
        sintomas_usuario = [sintoma.strip() for sintoma in texto_msg.split(";")]
    
    else:
        sintomas_usuario = [texto_msg]
            
    fichas_usuarios = Abrir_Conversas_Iniciadas(docs_path)
    ficha_usuario = None
    for usuario in fichas_usuarios:
        if usuario[0] == mensagem.chat.id:
            ficha_usuario = usuario
    
    casos = Importar_Banco_Protocolo_Manchester(docs_path)
    casos_especificos = []
    
    for caso in casos:
        if caso[1] == ficha_usuario[1]:
            casos_especificos.append(caso)
    
    sintomas_PM = []
    classificacoes_PM = []
    
    for sintoma in sintomas_usuario:
        sint_correspondente = None
        maior_similaridade = 0
        classificacao = None
        
        sint_usu = model.encode(sintoma.lower(), convert_to_tensor = True)
        
        for i in range(0, len(casos_especificos)):
            sint_cor = model.encode(casos_especificos[i][2].lower(), convert_to_tensor = True)
            similaridade = util.pytorch_cos_sim(sint_usu, sint_cor).item()
            
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                sint_correspondente = casos_especificos[i][2]
                classificacao = casos_especificos[i][3]
        
        if maior_similaridade < 0.65:
            sintomas_PM.append(sintoma)
            classificacoes_PM.append("Azul")
        
        else:
            sintomas_PM.append(sint_correspondente)
            classificacoes_PM.append(classificacao)
    
    if "Vermelho" in classificacoes_PM:
        classificacao_PM = "Vermelho"
    
    elif "Laranja" in classificacoes_PM:
        classificacao_PM = "Laranja"
    
    elif "Amarelo" in classificacoes_PM:
        classificacao_PM = "Amarelo"
    
    elif "Verde" in classificacoes_PM:
        classificacao_PM = "Verde"
    
    else:
        classificacao_PM = "Azul"
    
    
    return sintomas_PM, classificacao_PM

