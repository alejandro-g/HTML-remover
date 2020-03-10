#extrae html de una X pagina y luego guarda su html en un input.txt
import requests
import re

r = requests.get("https://example.com")

text_file = open("Input.txt", "w")
text_file.write(r.text)
text_file.close()

r = "<p class='important'>This is an important text</p>"

def striphtml(r): 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', r)
    return cleantext
