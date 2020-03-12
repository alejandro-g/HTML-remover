#extrae html de una X pagina y luego guarda su html en un input.txt
import re

tweet = "<span class=css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0>Greetings employees of Halcyon. The Board would like to inform you that due to an unforeseen circumstance, Patch 1.3 will be releasing next week. We apologize for any inconvenience this will cause but appreciate your patience.</span>"

#se corre solo la primera vez para que se cree el file con el primer tweet
#text_file = open("Input.txt", "w")
#text_file.write(tweet)
#text_file.close()

def striphtml(r): 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', r)
    return cleantext

text_file = open("Input.txt", "a")
text_file.write(tweet)
text_file.close()

text_file = open("Input.txt", "a")
text_file.write(striphtml(tweet))
text_file.close() 