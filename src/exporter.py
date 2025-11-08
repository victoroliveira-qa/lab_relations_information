# src/exporter.py

import csv
import os
from datetime import datetime

# Define o nome do arquivo de log para dentro da pasta 'output'
FILE_NAME = "output/historico_chat.csv"
OUTPUT_DIR = os.path.dirname(FILE_NAME)

# Define os cabeçalhos da nossa planilha CSV
HEADERS = ["Timestamp", "Pergunta", "Resposta", "Fontes"]


def salvar_para_csv(pergunta, resposta, fontes):
    try:
        # Garante que o diretório de output exista
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fontes_str = ", ".join(fontes) if fontes else "N/A"
        data_row = [timestamp, pergunta, resposta, fontes_str]

        file_exists = os.path.isfile(FILE_NAME)

        with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(HEADERS)

            writer.writerow(data_row)

        return True, None

    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        return False, str(e)