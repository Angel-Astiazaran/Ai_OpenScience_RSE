import os
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
OUTPUT_FOLDER_XML = os.path.join(BASE_DIR, "output/xml")

def extract_abstracts():
    if not os.listdir(OUTPUT_FOLDER_XML):  # Si no hay XMLs
        print("⚠️ No hay XMLs. No se extraerán abstracts.")
        return ""

    abstracts = []
    for file in os.listdir(OUTPUT_FOLDER_XML):
        if file.endswith(".xml"):
            with open(os.path.join(OUTPUT_FOLDER_XML, file), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "xml")
                abstract = soup.find("abstract")
                if abstract:
                    abstracts.append(abstract.get_text())
    return " ".join(abstracts)

def generate_wordcloud(text):
    output_path = os.path.join(OUTPUT_FOLDER, "wordcloud.png")
    
    if not text.strip():  # Si no hay texto, generar una imagen vacía
        print("⚠️ No hay texto. Generando wordcloud vacío.")
        plt.figure(figsize=(10, 5))
        plt.imshow([[1]], cmap="gray", aspect="auto")  # Imagen en blanco
    else:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")

    plt.axis("off")
    plt.savefig(output_path, dpi=300)
    print(f"✅ Word cloud guardada en: {output_path}")

    plt.clf()
    plt.close()

if __name__ == "__main__":
    text = extract_abstracts()
    generate_wordcloud(text)
