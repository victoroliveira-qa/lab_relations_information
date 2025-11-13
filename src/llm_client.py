# llm_client.py

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


def configurar_api_gemini():
    # ... (nenhuma mudança nesta função)
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            st.error("API Key 'GEMINI_API_KEY' não encontrada.")
            st.info(
                "Por favor, crie um arquivo `.env` na raiz do projeto e adicione a linha: GEMINI_API_KEY='SUA_CHAVE_AQUI'")
            return False
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"Erro ao configurar a API Key do Gemini: {e}")
        return False


def gerar_resposta_com_gemini(query, contexto):
    """
    Envia a query e o contexto recuperado para o Gemini Pro.
    """

    # --- PROMPT MODIFICADO PARA SER MAIS RIGOROSO ---
    prompt = f"""
    Você é um assistente especializado em análise de documentos financeiros.
    Seu trabalho é analisar o **Contexto Recuperado** abaixo e responder à **Pergunta do Usuário**.

    **Contexto Recuperado dos Documentos:**
    {contexto}

    **Pergunta do Usuário:**
    {query}

    **Instruções Rigorosas de Formatação:**
    1.  Sua tarefa é extrair a informação pedida para CADA documento fonte (empresa) mencionado no contexto.
    2.  Liste a resposta para CADA empresa em uma linha separada, usando um marcador (bullet point).
    3.  Se a informação exata (ex: o número) não for encontrada no trecho de contexto daquela empresa, você DEVE escrever: "[Nome da Empresa]: Informação não encontrada no trecho fornecido."
    4.  Não omita nenhuma empresa que esteja no contexto.
    5.  Se sua pesquisa trouxer mais uma informação para mesma empresa, liste as informações uma abaixo da outra.

    **Exemplo de Resposta Esperada:**
    * Empresa A: R$ 100 milhões.
    * Empresa B: R$ 200 milhões.
    * Empresa C: Informação não encontrada no trecho fornecido.
    * Empresa D: A receita proveio de X e Y. (Se o número não for encontrado, mas uma descrição sim)

    **Resposta:**
    """

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Erro ao chamar a API do Gemini: {e}")
        return "Desculpe, ocorreu um erro ao tentar gerar a resposta."