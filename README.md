🧠 Extração de Informações em PDF Financeiros — Usando RAG e APIs de IA (Gemini)

Este repositório contém a estrutura e os scripts utilizados para explorar e aplicar modelos de IA generativa (Gemini) no contexto do Mestrado em Informática Aplicada.
O projeto está organizado em módulos para facilitar:

* Leitura de PDF com RAG
* Interface gráfica usando Streamlit
* Consulta e validação de dados usando o Gemini.
---
## 👥 Integrantes

* **Camila Nunes**
* **Guilherme Silva**
* **Mariana Xavier**
* **Rodrigo Brochardt**
* **Victor Oliveira**
---
## 📌 Pastas principais:

* src/exporter.py → Função para realizar a exportação para o csv.
* src/llm_client.py → Clientes de integração com Gemini (Google).
* src/pdf_processor.py → Realiza o processamento de leitura dos PDF.
* src/rag_core.py → Realiza o processamento do PDF para consulta usando o Gemini.

---
## 📌 Modelos Utilizados

* [**gemini-2.0-flash-lite**](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br#python)

## 🛠️ Configuração do Ambiente

📌 Instalar dependências
* **pip install -r requirements.txt**
* **Python 3.13**

📌 Configurar variáveis de ambiente
* Crie um arquivo .env na raiz com o seguinte conteúdo:
* GEMINI_API_KEY=sua_chave_gemini_aqui
