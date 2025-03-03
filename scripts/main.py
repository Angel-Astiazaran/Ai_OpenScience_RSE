import pdfToXML
import wordCloudGen
import count_figures
import extract_links

if __name__ == "__main__":
    print("🔄 Procesando PDFs con GROBID...")
    pdfToXML.pdfToXML()

    print("\n📝 Generando nube de palabras...")
    text = wordCloudGen.extract_abstracts()
    wordCloudGen.generate_wordcloud(text)

    print("\n📊 Contando figuras en los artículos...")
    figures_data = count_figures.count_figures()
    count_figures.plot_figures(figures_data)

    print("\n🔗 Extrayendo links de los artículos...")
    links_data = extract_links.extract_links()
    for article, links in links_data.items():
        print(f"{article}: {links}")
