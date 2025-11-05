🧠 Projeto de Mestrado — Integração com APIs de IA (GPT & Gemini)

Este repositório contém a estrutura e os scripts utilizados para explorar e aplicar modelos de IA generativa (como GPT e Gemini) no contexto do Mestrado em Informática Aplicada.
O projeto está organizado em módulos para facilitar:

* Chamadas básicas às APIs
* Chamadas com dados locais (arquivos)
* Chamadas específicas relacionadas à pesquisa de mestrado (extração de relações, processamento textual, geração de resumos, etc.)

---
## 👥 Integrantes

* **Victor Henrique dos Santos Oliveira**
---
## 📌 Pastas principais:

* src/config → Configuração de chaves de API e variáveis de ambiente.
* src/clients → Clientes de integração com GPT (OpenAI) e Gemini (Google).
* src/chamadas_basicas → Exemplos simples de prompts e respostas para aprendizado.
* src/chamadas_com_arquivos → Exemplos de uso das APIs com dados locais (CSV, TXT etc).
* src/chamadas_trabalho → Scripts utilizados nas etapas da pesquisa de mestrado (processamento, extração, análise, etc).
---
## 🤖 Como Rodar os Exemplos

* Deve acessar a pasta raiz do projeto.

📌 Exemplo de chamada básica ao GPT / Gemini
* python -m projeto_gemini.chamada_gemini_basica

📌 Exemplo de chamada ao GPT com CSV
* python -m projeto_gemini.chamada_gemini_basica

📌 Exemplo de extração de relações (Mestrado)
*  python -m projeto_gemini.chamada_gemini_basica
---
## 📌 Modelos Utilizados

* [**OpenAI GPT-5**](https://platform.openai.com/docs/models/gpt-5)
* [**Gemini 2.5 Flash**](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br#python)

## 🛠️ Configuração do Ambiente

📌 Instalar dependências
* **pip install -r requirements.txt**
* **Python 3.13**

📌 Configurar variáveis de ambiente
* Crie um arquivo .env na raiz com o seguinte conteúdo:
* OPENAI_API_KEY=sua_chave_openai_aqui
* GEMINI_API_KEY=sua_chave_gemini_aqui
