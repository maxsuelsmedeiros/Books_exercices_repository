def main():
    ###The function returns True the list of letters passed is used to form a word
    bag_of_words=open("exemplos/words.txt")
    def uses_only(word,letters_to_verify):
        for l in letters_to_verify:
            if l not in word:
                return False
        return True
    print(uses_only("papagaio","paio"))


if __name__=='__main__':
    main()