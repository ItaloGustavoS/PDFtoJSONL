import PyMuPDF as fitz
import json


# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_list = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        text_list.append({"page": page_num + 1, "text": text})
    return text_list


# Função para escrever dados em um arquivo JSONL
def write_jsonl(data, filename):
    with open(filename, "w") as file:
        for item in data:
            json_line = json.dumps(item)
            file.write(json_line + "\n")


# Caminhos dos PDFs
pdf_paths = ["datawindow_reference_v2021.pdf", "powerscript_reference_v2021.pdf"]

# Gerar arquivos JSONL para cada PDF
for pdf_path in pdf_paths:
    data = extract_text_from_pdf(pdf_path)
    jsonl_filename = pdf_path.replace(".pdf", ".jsonl")
    write_jsonl(data, jsonl_filename)
    print(f"Arquivo {jsonl_filename} gerado com sucesso!")
