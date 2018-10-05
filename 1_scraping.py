#! python3
import urllib.request

url = "https://www.etsisi.upm.es/estudios/secretaria-alumnos"
r = urllib.request.urlopen(url)
print("Status code: %d, length: %d bytes" % (r.status, len(r.read())))
