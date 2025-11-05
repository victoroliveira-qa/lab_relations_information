import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

# Caminhos
PDF_DIR = "data/pdfs"
VECTOR_DIR = "data/vector_store"
os.makedirs(VECTOR_DIR, exist_ok=True)

# Modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Extrai texto dos PDFs
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with open(caminho_pdf, "rb") as f:
        reader = PdfReader(f)
        for pagina in reader.pages:
            texto += pagina.extract_text() or ""
    return texto

# Coleta e indexa todos os PDFs
documentos = []
metadados = []

for arquivo in os.listdir(PDF_DIR):
    if arquivo.endswith(".pdf"):
        caminho = os.path.join(PDF_DIR, arquivo)
        texto = extrair_texto_pdf(caminho)
        documentos.append(texto)
        metadados.append({"arquivo": arquivo})

print(f"🔍 {len(documentos)} documentos encontrados para indexação.")

# Gera embeddings
embeddings = modelo.encode(documentos, show_progress_bar=True)

# Cria e salva índice FAISS
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

faiss.write_index(index, os.path.join(VECTOR_DIR, "index.faiss"))

with open(os.path.join(VECTOR_DIR, "metadados.pkl"), "wb") as f:
    pickle.dump(metadados, f)

print("✅ Indexação concluída e salva em data/vector_store/")
