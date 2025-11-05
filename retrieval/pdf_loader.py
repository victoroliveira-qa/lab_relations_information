import os
from PyPDF2 import PdfReader

def carregar_pdfs(diretorio):
    textos = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(diretorio, arquivo)
            reader = PdfReader(caminho)
            texto = ""
            for page in reader.pages:
                texto += page.extract_text() + "\n"
            textos.append({"nome": arquivo, "conteudo": texto})
    return textos
