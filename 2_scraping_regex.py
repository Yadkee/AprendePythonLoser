#! python3
import urllib.request
import re

url = "https://www.etsisi.upm.es/estudios/secretaria-alumnos"
r = urllib.request.urlopen(url)
web = r.read().decode()  # html en texto plano

# Buscamos en la tercera row de la tabla principal
tr = re.findall("<tr>(.*?)</tr>", web, flags=re.DOTALL)[2]

for i in re.findall("<li.*?>(.*?)</li>", tr, flags=re.DOTALL):
    # Cada una de las noticias de ACTUALIDAD
    print(re.sub("<.*?>", "", i, flags=re.DOTALL))  # Quita todas las tags
