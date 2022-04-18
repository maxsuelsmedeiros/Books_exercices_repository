def main():
    def rotate_word(word,num):
        rotation=0
        if num>=1 and num<=26:
            rotation=num
        elif num<=-1 and num>=-26:
            rotation=num
        else:
            print("valor não é valido, insira um novo valor.")
            return
        cesar=""
        for letter in word:

        ###Cifra de Cesar para letras minúsculas
            if rotation>0:
                if ord(letter)+rotation<=122:
                    cesar=cesar+chr(ord(letter)+rotation)
                else:
                    leftover=(ord(letter)+rotation)-122
                    cesar=cesar+chr(leftover+96)
            else:
                if ord(letter)-abs(rotation)>=97:
                    cesar=cesar+(chr(ord(letter)-abs(rotation)))
                else:
                    leftover=(ord(letter)-abs(rotation))
                    cesar=cesar+chr((leftover-97)+123)
        return cesar
    def joke(joke):
        split_joke=joke.split()
        decoded_joke=""
        for word in split_joke:
            decoded_joke=decoded_joke+" "+rotate_word(word,13)
        return decoded_joke
                
    print(joke("Obl, gung jnf gur shaavrfg wbxr V rire urneq"))
    

if __name__=='__main__':
    main()