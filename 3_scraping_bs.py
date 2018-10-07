#! python3
import urllib.request
import bs4

url = "https://www.etsisi.upm.es/estudios/secretaria-alumnos"
r = urllib.request.urlopen(url)
web = r.read()  # html binario

soup = bs4.BeautifulSoup(web, "html.parser")
tr = soup.findAll("tr")[2]  # Buscamos en la tercera row de la tabla principal

for i in tr.findAll("li"):
    print(i.text)  # Cada una de las noticias de ACTUALIDAD en texto plano :D
