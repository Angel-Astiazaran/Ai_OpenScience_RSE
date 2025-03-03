import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
OUTPUT_FOLDER_XML = os.path.join(OUTPUT_FOLDER, "xml")
LINKS_FILE = os.path.join(OUTPUT_FOLDER, "extracted_links.txt")

def extract_links():
    if not os.listdir(OUTPUT_FOLDER_XML):  # Si no hay XMLs, retorna diccionario vacío
        return {}

    links = {}
    for file in os.listdir(OUTPUT_FOLDER_XML):
        if file.endswith(".xml"):
            with open(os.path.join(OUTPUT_FOLDER_XML, file), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "xml")

                web_references = soup.find_all("ref", {"type": "web"})
                link_tags = soup.find_all("ptr") + soup.find_all("a")

                found_links = [ref.get_text().strip() for ref in web_references if ref.get_text().startswith("http")]
                found_links += [link["target"].strip() for link in link_tags if "target" in link.attrs and link["target"].startswith("http")]

                if found_links:
                    links[file] = found_links

    return links

def save_links(links):
    if not links:
        # Si no hay links, vacía el archivo (elimina su contenido)
        open(LINKS_FILE, "w", encoding="utf-8").close()
        return  

    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        for article, urls in links.items():
            f.write(f"{article}:\n")
            for url in urls:
                f.write(f"  - {url}\n")
            f.write("\n")

if __name__ == "__main__":
    links_data = extract_links()
    save_links(links_data)
