import faiss
import numpy as np
import os
import pickle
from google import genai

from config.settings import GEMINI_API_KEY

# Criação do cliente apenas para embeddings
client = genai.Client(api_key=GEMINI_API_KEY)

def criar_embeddings(textos, save_path="data/vector_store/index.faiss"):
    texts = [t["conteudo"] for t in textos]
    response = client.models.embed_content(
        model="text-embedding-004",
        contents=texts
    )

    embeddings = np.array([r.values for r in response.embeddings]).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, save_path)

    metadados = [{"nome": t["nome"], "conteudo": t["conteudo"]} for t in textos]
    with open(save_path.replace(".faiss", ".pkl"), "wb") as f:
        pickle.dump(metadados, f)

def carregar_vector_store():
    index = faiss.read_index("data/vector_store/index.faiss")
    with open("data/vector_store/index.pkl", "rb") as f:
        metadados = pickle.load(f)
    return index, metadados
