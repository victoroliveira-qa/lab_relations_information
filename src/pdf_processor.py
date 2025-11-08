# pdf_processor.py

import fitz  # PyMuPDF
import os


def extrair_texto_e_metadados(pdf_path):
    """
    Extrai texto de um PDF, página por página, e anexa metadados.

    Retorna:
        Uma lista de dicionários, onde cada dicionário representa
        uma página (um "chunk" de documento).
    """
    doc_chunks = []

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Erro ao tentar abrir o arquivo {pdf_path}: {e}")
        return []  # Retorna lista vazia se não puder abrir

    file_name = os.path.basename(pdf_path)

    for page_num, page in enumerate(doc):
        text = page.get_text()
        if text:  # Só processa se a página tiver texto
            doc_chunks.append({
                "texto": text,
                "fonte": file_name,
                "pagina": page_num + 1
            })

    doc.close()
    return doc_chunks