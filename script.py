#extrae html de una X pagina y luego guarda su html en un input.txt
import requests

r = requests.get("https://example.com")

text_file = open("Input.txt", "w")
text_file.write(r.text)
text_file.close()

