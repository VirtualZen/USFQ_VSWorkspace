import time

import pandas as pd  # type: ignore[import-unresolved]
import requests  # type: ignore[import-unresolved]
from bs4 import BeautifulSoup  # type: ignore[import-unresolved]

BASE = "https://books.toscrape.com/"

datos = []
for pagina in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for libro in soup.select("article.product_pod"):
        datos.append({
        "titulo": libro.h3.a["title"],
        "precio": libro.select_one("p.price_color").text,
        "rating": " ".join(libro.select_one("p.star-rating")["class"])
        })
        print("\t",datos[-1]["titulo"], datos[-1]["precio"], datos[-1]["rating"], flush=True)
    print(f"Página {pagina}/50", flush=True)
    time.sleep(0.5)
print("Scraping completed. Part 1 no category added. Wait ...", flush=True)
def mapa_de_categorias(): # te la damos hecha
    sopa = BeautifulSoup(requests.get(BASE).text, "html.parser")
    mapa = {}
    for a in sopa.select("div.side_categories ul ul li a"):
        nombre, url = a.text.strip(), BASE + a["href"]
        print(f"\tCategoría: {nombre}", flush=True)
        while url:
            s = BeautifulSoup(requests.get(url).text, "html.parser")
            for libro in s.select("article.product_pod"):
                mapa[libro.h3.a["title"]] = nombre
            sig = s.select_one("li.next a")
            url = url.rsplit("/", 1)[0] + "/" + sig["href"] if sig else None
            time.sleep(0.5)
    return mapa

print("Mapping categories...", flush=True)
libros = pd.DataFrame(datos)
libros["categoria"] = libros["titulo"].map(mapa_de_categorias())
print("Categories mapped.", flush=True)
print()
print(len(libros), "libros")
print(libros["categoria"].isna().sum(), "sin categoría")
libros.to_csv("libros.csv", index=False)



## código anterior
def old_code():
    datos = []
    for pagina in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        for libro in soup.select("article.product_pod"):
            datos.append({
            "titulo": libro.h3.a["title"],
            "precio": libro.select_one("p.price_color").text,
            "rating": " ".join(libro.select_one("p.star-rating")["class"])
            })
            print("\t",datos[-1]["titulo"], datos[-1]["precio"], datos[-1]["rating"])
        print(f"Página {pagina}/50")
        time.sleep(0.5)
        return datos
