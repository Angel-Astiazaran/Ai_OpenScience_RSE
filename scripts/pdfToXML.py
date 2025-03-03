import os
import requests

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output/xml")

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def pdfToXML():
    for pdf in os.listdir(PDF_FOLDER):
        if pdf.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, pdf)
            files = {"input": open(pdf_path, "rb")}
            response = requests.post(GROBID_URL, files=files, data={"consolidate": "1"})  

            if response.status_code == 200:
                output_path = os.path.join(OUTPUT_FOLDER, pdf.replace(".pdf", ".xml"))
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"✅ Procesado: {pdf}")
            else:
                print(f"❌ Error con {pdf}: {response.status_code}")

if __name__ == "__main__":
    pdfToXML()
