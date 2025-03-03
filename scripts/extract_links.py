import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.expanduser("~/Desktop/Ai/Ai_OpenScience_RSE")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

def extract_links():
    links = {}
    for file in os.listdir(OUTPUT_FOLDER):
        if file.endswith(".xml"):
            with open(os.path.join(OUTPUT_FOLDER, file), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "lxml")
                web_references = soup.find_all("ref", {"type": "web"})
                links[file] = [ref.get_text() for ref in web_references if ref.get_text().startswith("http")]

    return links

if __name__ == "__main__":
    links_data = extract_links()
    for article, links in links_data.items():
        print(f"{article}: {links}")
