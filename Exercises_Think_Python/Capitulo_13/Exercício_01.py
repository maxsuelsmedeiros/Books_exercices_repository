import string
import re
import unidecode
def main():
    texto=open("/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/texto_simples.txt")
    texto=texto.readline()
    texto_editado=""
    for i in texto.split(" "):
        #breaking the line
        texto_editado+=i+"\n"
        #eliminating the whitespaces
        texto_editado=texto_editado.replace(" ","")
        #turning all letters in lower case
        texto_editado=texto_editado.lower()

        #removing the ponctuations
        texto_editado=re.sub(r'[^\w\s]', '',texto_editado)
        #removing the accent from the letters
        
        texto_editado=unidecode.unidecode(texto_editado)
    print(texto_editado)
if __name__=='__main__':
    main()