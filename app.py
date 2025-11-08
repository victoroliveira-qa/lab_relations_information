# app.py

import streamlit as st
# Imports agora apontam para o pacote 'src'
from src.rag_core import carregar_e_indexar_pdfs, recuperar_contexto
from src.llm_client import configurar_api_gemini, gerar_resposta_com_gemini
from src.exporter import salvar_para_csv

# --- 1. Configuração da Página ---
st.set_page_config(
    page_title="Chat com Documentos Financeiros",
    page_icon="💸"
)
st.title("💸 Chat RAG com Documentos Financeiros")
st.caption("Pergunte sobre os 10 documentos financeiros fornecidos.")

# --- 2. Configuração da API Key ---
if not configurar_api_gemini():
    st.stop()

# --- 3. Carregamento e Indexação (RAG Core) ---
bm25_index, all_chunks = carregar_e_indexar_pdfs()

if bm25_index is None or all_chunks is None:
    st.error("O pipeline RAG não pôde ser inicializado. Verifique os logs e a pasta 'data/pdfs'.")
    st.stop()

# --- 4. Interface de Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant",
                                  "content": "Olá! Estou pronto para responder perguntas sobre seus documentos financeiros."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qual o valor total de..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pesquisando nos documentos..."):
            contexto, fontes = recuperar_contexto(prompt, bm25_index, all_chunks)

        with st.spinner("Gerando resposta com IA..."):
            resposta_ia = gerar_resposta_com_gemini(prompt, contexto)

            if fontes:
                resposta_final_display = resposta_ia + "\n\n*Fontes consultadas: " + ", ".join(fontes) + "*"
            else:
                resposta_final_display = resposta_ia

            st.markdown(resposta_final_display)

            # --- 3. Exportação ---
            sucesso, erro = salvar_para_csv(prompt, resposta_ia, fontes)

            if sucesso:
                st.success("Seu arquivo foi processado e está salvo em 'output/historico_chat.csv'")
            else:
                st.error(f"Falha ao salvar o histórico: {erro}")

    st.session_state.messages.append({"role": "assistant", "content": resposta_final_display})