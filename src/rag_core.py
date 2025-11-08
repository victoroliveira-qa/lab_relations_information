# src/rag_core.py

import os
import streamlit as st
from rank_bm25 import BM25Okapi
# Import agora é relativo ao pacote 'src'
from src.pdf_processor import extrair_texto_e_metadados

# Caminho do diretório de PDFs foi atualizado
PDF_DIR = "data/pdfs"


@st.cache_resource(show_spinner="Processando PDFs... (Isso só acontece uma vez)")
def carregar_e_indexar_pdfs():
    if not os.path.exists(PDF_DIR):
        st.error(f"O diretório '{PDF_DIR}' não foi encontrado.")
        return None, None

    # ... (O resto da função continua igual) ...
    arquivos_pdf = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]
    if not arquivos_pdf:
        st.error(f"Nenhum arquivo PDF encontrado em '{PDF_DIR}'.")
        return None, None

    todos_chunks = []
    with st.spinner(f"Processando {len(arquivos_pdf)} PDFs..."):
        for pdf_file in arquivos_pdf:
            pdf_path = os.path.join(PDF_DIR, pdf_file)
            todos_chunks.extend(extrair_texto_e_metadados(pdf_path))

    if not todos_chunks:
        st.error("Nenhum texto pôde ser extraído dos PDFs. Verifique os arquivos.")
        return None, None

    text_corpus = [chunk["texto"] for chunk in todos_chunks]
    tokenized_corpus = [doc.lower().split() for doc in text_corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    st.success(f"{len(arquivos_pdf)} PDFs e {len(todos_chunks)} páginas indexadas com sucesso!")
    return bm25, todos_chunks


def recuperar_contexto(query, bm25_index, all_chunks, top_k=20):
    # ... (Nenhuma mudança nesta função) ...
    tokenized_query = query.lower().split()
    scores = bm25_index.get_scores(tokenized_query)
    top_k_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

    contexto = ""
    fontes_usadas = set()

    for i in top_k_indices:
        chunk = all_chunks[i]
        contexto += f"---\nFonte: {chunk['fonte']} (Página {chunk['pagina']})\n"
        contexto += chunk['texto'] + "\n---\n"
        fontes_usadas.add(f"{chunk['fonte']} (Pág. {chunk['pagina']})")

    return contexto, list(fontes_usadas)