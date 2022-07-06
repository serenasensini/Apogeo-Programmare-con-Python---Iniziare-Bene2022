import pandas as pd
from bs4 import BeautifulSoup
import requests as req

# page = req.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
#
# print(page)
#
# soup = BeautifulSoup(page.content, "html.parser")
#
# # print(soup)
# # print(soup.prettify())
#
# lista_paragrafi = soup.find_all("p")
# print(lista_paragrafi)
#
# testo = lista_paragrafi[0].get_text()
# print(testo)

page = req.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

lista_paragrafi = soup.find_all("p")
# print(lista_paragrafi)

# for paragrafo in lista_paragrafi:
    # print(paragrafo.get_text())

lista_paragrafi_con_classe = soup.find_all("p", class_="inner-text")
# print(lista_paragrafi_con_classe)

# for paragrafo in lista_paragrafi_con_classe:
    # print(paragrafo.get_text())

page_reviews = req.get("https://www.imdb.com/title/tt4901306/reviews?ref_=tt_urv")

# PUNTEGGIO
# TITOLO RECENSIONE
# DATA
# CONTENUTO

pagina = BeautifulSoup(page_reviews.content, "html.parser")

# print(pagina.prettify())

titoli = pagina.find_all("a", class_="title")

# print(titoli)

date = pagina.find_all("span", class_="review-date")

# print(date)

punteggi = pagina.find_all("span", class_="rating-other-user-rating")

# print(punteggi)

contenuti = pagina.find_all("div", class_="text show-more__control")

# print(contenuti)


titoli_testo = []

for testo in titoli:
    titoli_testo.append(testo.get_text().replace("\n", ""))

# print(titoli_testo)

date_testo = []

for testo in date:
    date_testo.append(testo.get_text())

# print(date_testo)

recensioni_testo = []

for testo in contenuti:
    print(testo)
    recensioni_testo.append(str(testo.get_text().replace("\n", "")))

print(recensioni_testo)

punteggi_testo = []

for testo in pagina.find_all("span", class_="rating-other-user-rating"):
    span = testo.find_all("span")
    punteggi_testo.append(span[0].get_text())
    # for punteggio in testo.find_all("span"):
    #     print(punteggio)

# print(punteggi_testo)
# NON FARLO
punteggi_testo.append("9")

print(len(date_testo))
print(len(titoli_testo))
print(len(recensioni_testo))
print(len(punteggi_testo))

dataframe = pd.DataFrame({
    "date": date_testo,
    "titles": titoli_testo,
    "reviews": recensioni_testo,
    "score": punteggi_testo
})


print(dataframe.head())

dataframe.to_csv("recensioni.csv")