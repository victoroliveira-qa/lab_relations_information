import os
import PyPDF2
from clients.gemini_client import gemini_generate

def extrair_texto_pdf(caminho_pdf: str) -> str:

    texto = ""
    with open(caminho_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            texto += page.extract_text() or ""
    return texto


def consultar_documentos_financeiros(pergunta: str):
    """
    Faz uma consulta em todos os PDFs da pasta 'docs' e salva as respostas em 'resultados/respostas.txt'.
    """
    prompt_base = f"""
    Você é um assistente especializado em extração de informações de documentos financeiros.

    Analise o texto extraído de um PDF.
    
    Sua tarefa:
    1. Localize o conteúdo referente à pergunta abaixo.
    2. Extraia somente o valor solicitado.

    Pergunta: {pergunta}
    """

    resultados = []

    # Iterar sobre todos os PDFs
    for arquivo in os.listdir("docs"):
        if arquivo.lower().endswith(".pdf"):
            caminho_pdf = os.path.join("docs", arquivo)
            texto = extrair_texto_pdf(caminho_pdf)

            # Enviar para o modelo Gemini
            prompt = f"{prompt_base}\n\nTexto do documento ({arquivo}):\n{texto}"
            resposta = gemini_generate(prompt)

            nome_empresa = os.path.splitext(arquivo)[0].replace("_", " ").upper()
            resultado_formatado = f"Na empresa: {nome_empresa}, {resposta}"
            resultados.append(resultado_formatado)

            print(resultado_formatado)
            print("-" * 80)

    # Salvar em arquivo
    os.makedirs("resultados", exist_ok=True)
    with open("resultados/respostas.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(resultados))


if __name__ == "__main__":
    pergunta = input("Digite sua pergunta sobre os documentos financeiros: ")
    consultar_documentos_financeiros(pergunta)
