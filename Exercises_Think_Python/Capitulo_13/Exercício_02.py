from unidecode import unidecode


import unidecode
import re

def main():
    #clean the data from the ponctuation,accents 
    def clear_book(book):
        #change all into lower case
        book=str(book).lower()
        #removing the ponctuation
        book=re.sub(r'[^\w\s]', '',book)
        #removing the accents 
        book=unidecode.unidecode(book)
        #separating the words
        new_book=book.split(" ")
        return new_book
    def number_of_words(book):
        count_words=dict()
        for word in book:
            count_words[word]=count_words.get(word,0)+1
        count_words=sorted(count_words.items(),key=lambda x: x[1],reverse=True)
        if '' in count_words: del count_words['']
        return count_words

    #oppening the LITTLE HICKORY book
    gut_lh=open("/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/gut.txt")
    book_lh=[]
    #removing the words not related oo the LITTLE HICKORY book
    for index,line in enumerate(gut_lh):
        if index>=79 and index<5733:
            book_lh.append(str(line).rstrip("\n"))
    print(number_of_words(clear_book(book_lh)))

if __name__=='__main__':
    main()