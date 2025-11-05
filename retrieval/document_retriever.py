import numpy as np
from google import genai
from config.settings import GEMINI_API_KEY
from retrieval.vector_store import carregar_vector_store

client = genai.Client(api_key=GEMINI_API_KEY)

def buscar_trechos_relevantes(pergunta, top_k=3):
    index, metadados = carregar_vector_store()

    # Cria embedding da pergunta
    emb = client.models.embed_content(
        model="text-embedding-004",
        contents=[pergunta]
    ).embeddings[0].values

    emb = np.array([emb]).astype("float32")

    # Busca os k documentos mais próximos
    distances, indices = index.search(emb, top_k)

    resultados = []
    for idx in indices[0]:
        resultados.append(metadados[idx]["conteudo"][:2000])  # Limita tamanho do trecho

    return "\n\n".join(resultados)
