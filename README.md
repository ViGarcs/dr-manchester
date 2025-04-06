# 🤖 Dr. Manchester - Chatbot do Protocolo de Manchester
Este é um chatbot desenvolvido em Python que auxilia na classificação de sintomas com base no **Protocolo de Manchester**. Com base em um banco de dados clínico e técnicas de NLP, ele recebe os sintomas relatados por usuários via Telegram, analisa os sintomas descritos e sugere uma classificação de prioridade, auxiliando no processo de triagem.

---

## Funcionalidades

- Processa entradas em linguagem natural.
- Identifica sintomas e associa à categoria clínica correspondente.
- Garante que sintomas críticos tenham prioridade adequada.
- Classifica com base na **urgência mais alta** entre os sintomas identificados.

---

## Tecnologias usadas

- **Python 3**
- **MySQL** (para armazenar dados de usuários e sintomas)
- **Telegram Bot API** (via `pyTelegramBotAPI`)
- **NLP com Sentence Transformers** (`sentence-transformers`)

---

## Instalação

> Antes de começar, você precisa ter **Python 3.8+** ou **Python 3.11-** (as versões 3.12+ do python ainda não possuem o suporte necessario para algumas bibliotecas do projeto), **MySQL** e **pip** instalados no seu sistema.

### 1. Clone o repositório:

```bash
git clone https://github.com/ViGarcs/dr-manchester.git
cd dr-manchester
```

### 2. Instale as dependências:

pip install -r requirements.txt

### 3. Configure seu token do telegram:

1. Vá até o BotFather no Telegram e crie seu próprio bot;
2. Copie o token fornecido
3. Crie um arquivo chamado ".env" (sem as aspas) na raiz do projeto e adicione:

TELEGRAM_TOKEN = "seu_token_aqui" (com as aspas)

> ⚠️ Nunca compartilhe seu token publicamente!

### 4. Execute o bot:

python main.py

---

## 📄 Licença
Projeto criado apenas para fins educacionais e portfólio. Não autorizado para uso comercial sem permissão prévia.

