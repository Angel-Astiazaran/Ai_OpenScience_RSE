import os
import requests

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output/xml")

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def delete_existing_xml():
    """Elimina todos los XMLs en la carpeta de salida."""
    for file in os.listdir(OUTPUT_FOLDER):
        if file.endswith(".xml"):
            os.remove(os.path.join(OUTPUT_FOLDER, file))

def pdfToXML():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

    if not pdf_files:
        delete_existing_xml()  # Si no hay PDFs, borra cualquier XML existente.
        return  

    for pdf in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, pdf)
        files = {"input": open(pdf_path, "rb")}
        response = requests.post(GROBID_URL, files=files, data={"consolidate": "1"})  

        if response.status_code == 200:
            output_path = os.path.join(OUTPUT_FOLDER, pdf.replace(".pdf", ".xml"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(response.text)

if __name__ == "__main__":
    pdfToXML()
