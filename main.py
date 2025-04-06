# ===== DEPENDENCIAS =====
# pip install pytelegrambotapi
# pip install sentence-transformers
# pip install python-dotenv

# ===== INSTALACAO DAS DEPENDENCIAS =====
import subprocess

subprocess.run("pip install accelerate", shell=True)
subprocess.run("pip install -U sentence-transformers", shell=True)
subprocess.run("pip install pyTelegramBotAPI", shell=True)
subprocess.run("pip install python-dotenv", shell=True)

# ===== BIBLIOTECA =====
# -- BIBLIOTECAS EXTERNAS --
import telebot                      # Interacao com o bot do Telegram
from dotenv import load_dotenv
import os

# -- MÓDULOS INTERNOS DO PROJETO --
# Arquivo com os caminhos dos documentos utilizados
from Caminhos import docs_path

# Funcoes de interacao com a lista de usuarios com coversas em aberto
from Funcoes_Conversas_Iniciadas import Excluir_Usuario_Conver_Ini

# Funcoes logicas: Apoiam as funcoes de comunicacao com o Telegram
from Funcoes_Comunicacao_Telegram import Verifica_Funcao_Pos_Categoria
from Funcoes_Comunicacao_Telegram import Verificar_Mensagem_Pos_Sintomas
from Funcoes_Comunicacao_Telegram import Verificar_Mensagem_Inicial

# Funcoes de tratamento de mensagens do usuario
from Tratamento_Mensagens_Usuarios import Filtro_Mensagens_Usuario

# ===== VARIAVEIS GLOBAIS =====
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
   
# ===== PROGRAMA PRINCIPAL =====
# -- Handlers para a chamada da função de resposta ao usuario --
def Handler_Verificar_Mensagem_Pos_Sintomas(mensagem):
    return Verificar_Mensagem_Pos_Sintomas(mensagem, docs_path)

def Handler_Verifica_Funcao_Pos_Categoria(mensagem):
    return Verifica_Funcao_Pos_Categoria(mensagem, docs_path)

def Handler_Verificar_Mensagem_Inicial(mensagem):
    return Verificar_Mensagem_Inicial(mensagem, docs_path)

# -- Interacao com o usuario --
@bot.message_handler(func = Handler_Verificar_Mensagem_Pos_Sintomas)
def Envia_Mensagem_Classificacao(mensagem):
    sintomas_PM, classificacao_PM = Filtro_Mensagens_Usuario(mensagem, docs_path)
    texto_teste = "Os sintomas informados são:\n- " + "\n- ".join(sintomas_PM) + "\n\nLevando esses dados em consideração, a classificação mais adequada é: {}".format(classificacao_PM)
    
    Excluir_Usuario_Conver_Ini(mensagem.chat.id, docs_path)
    bot.send_message(mensagem.chat.id, texto_teste)
    
@bot.message_handler(func = Handler_Verifica_Funcao_Pos_Categoria)
def Envia_Mensagem_Sintomas(mensagem):
    texto = "Certo, agora me diga usando palavras-chave, os sintomas que está sentindo.\nSe estiver sentindo mais de um sintoma, separe-os com ';' (ponto e vírgula)" 
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(func = Handler_Verificar_Mensagem_Inicial)
def Envia_Mensagem_Inicial(mensagem):
    texto = """Ola, eu sou o Dr. Manchester, estou aqui para ajudar a entender melhor a sua situação. Vamos começar?

Qual das seguintes categorias melhor define o seu caso (Clique na opção desejada)?
/Alergia
/Asma
/Autoagressao
/Bebe_Chorando
/Cefaleia
/Convulsoes
/Desmaio
/Diarreia_e_ou_vomitos
/Dispneia_em_adulto
/Dispneia_em_crianca
/Dor_abdominal_em_adulto
/Dor_abdominal_em_crianca
/Dor_de_garganta
/Dor_lombar
/Dor_toracica
/Mal_estar_em_adulto
/Pais_preocupados
/Quedas
/Trauma_cranioencefalico
/Trauma_maior

            """
    bot.send_message(mensagem.chat.id, texto)



bot.polling() # Lendo continuamente as mensagens enviadas pelo Telegram

