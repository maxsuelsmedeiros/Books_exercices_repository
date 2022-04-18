def main():
    ###Create a list with the alfabet with only lower case
    def alfabet_minor():
        alfabet=[]
        for i in range(26):
            alfabet.append(chr(97+i))
        return alfabet
    ### Create a list with the combination of the n elements
    def forbidden_n_letters(num_of_comb):

        alfabet=alfabet_minor()
        forbidden_comb=combinations(alfabet,num_of_comb)
        forbidden_letters=list(forbidden_comb)
        return forbidden_letters
    ### Returns the 5 combination letters with the list words affected
    def min_affected_words(bag_of_words):
        bag=bag_of_words.readlines()
        num_words_affected=0
        list_of_num_words_affected=[]
        forbidden_5=forbidden_n_letters(5)
        for forbidden_letters in forbidden_5:
            num_words_affected=0
            for word in bag:
                print(word,forbidden_letters)
                if avoids(word,forbidden_letters) is True:
                    num_words_affected=num_words_affected+1
            list_of_num_words_affected.append(num_words_affected)

        position_min_value_affected=list_of_num_words_affected.index(min(list_of_num_words_affected))
        forbidden_5_less_excluding=forbidden_5[position_min_value_affected]
        return forbidden_5_less_excluding, min(list_of_num_words_affected)

if __name__=='__main__':
    main()