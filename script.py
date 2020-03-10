#extrae html de una X pagina y luego guarda su html en un input.txt
import requests
import re

r = requests.get("https://python.org")

text_file = open("Input.txt", "w")
text_file.write(r.text)
text_file.close()


def striphtml(r): 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', r)
    return cleantext

text_file = open("Input.txt", "a")
text_file.write(striphtml(r.text))
text_file.close() 