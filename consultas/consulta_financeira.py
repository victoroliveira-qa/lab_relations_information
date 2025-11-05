import os
from clients.gemini_client import gemini_generate
from retrieval.document_retriever import buscar_trechos_relevantes

def consultar_documentos_financeiros(pergunta):
    contexto = buscar_trechos_relevantes(pergunta)

    prompt = f"""
    Você é um assistente financeiro. 
    Baseando-se APENAS nas informações a seguir, responda à pergunta:

    Contexto:
    {contexto}

    Pergunta: {pergunta}
    """

    resposta = gemini_generate(prompt)

    # Salva em arquivo txt
    with open("resposta_consulta.txt", "w", encoding="utf-8") as f:
        f.write(f"Pergunta: {pergunta}\n\nResposta:\n{resposta}")

    print("✅ Resposta salva em resposta_consulta.txt")
    return resposta


if __name__ == "__main__":
    pergunta = input("Digite sua pergunta sobre os PDFs financeiros: ")
    consultar_documentos_financeiros(pergunta)
