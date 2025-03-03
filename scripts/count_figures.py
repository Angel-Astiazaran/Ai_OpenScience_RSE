import os
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
OUTPUT_FOLDER_XML = os.path.join(BASE_DIR, "output/xml")

def count_figures():
    figures_count = {}
    for file in os.listdir(OUTPUT_FOLDER_XML):  
        if file.endswith(".xml"):
            with open(os.path.join(OUTPUT_FOLDER_XML, file), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "xml")
                figures = soup.find_all("figure")
                figures_count[file] = len(figures)

    return figures_count


def plot_figures(figures_count):
    plt.figure(figsize=(10, 5))
    plt.bar(figures_count.keys(), figures_count.values(), color="blue")
    plt.xticks(rotation=90)
    plt.xlabel("Articles")
    plt.ylabel("Number of Figures")
    plt.title("Number of Figures per Article")
    
    output_path = os.path.join(OUTPUT_FOLDER, "figCounted.png")
    plt.savefig(output_path)  
    print(f"Fig Counter guardado en: {output_path}")

    plt.clf()  # Limpia la figura
    plt.close()  # Cierra la figura para evitar duplicaciones

if __name__ == "__main__":
    figures_data = count_figures()
    plot_figures(figures_data)
