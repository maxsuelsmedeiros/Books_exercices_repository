import re
def main():
    #Basic function created to read and clean the file with words in english
    bag=open("Exercises_Think_Python/words.txt")
    def remove_useless_simbols(bag):
        new_bag=[]
        for word in bag:
            word=word.strip("'")
            new_bag.append(word.strip("\n"))
        return new_bag
    bag_of_words=remove_useless_simbols(bag)
    def clear_book(book):
        #change all into lower case
        book=str(book).lower()
        #separating the words
        book=re.sub(r'[^\w\s]', '',book)
        new_book=book.split(" ")
        return new_book
    gut_lh=open("/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/gut.txt")
    book_lh=[]
    #removing the words not related oo the LITTLE HICKORY book
    for index,line in enumerate(gut_lh):
        if index>=79 and index<5733:
            book_lh.append(str(line).rstrip("\n"))
    book_lh=clear_book(book_lh)
    def how_many_are_not(bag_of_words,book):
        not_in_the_word_bag=[]
        for word in set(book):
            if word not in bag_of_words:
                not_in_the_word_bag.append(word)
        return not_in_the_word_bag
    print("The words that are not in the list of valid words are:\n",how_many_are_not(bag_of_words,book_lh))
if __name__=='__main__':
    main()