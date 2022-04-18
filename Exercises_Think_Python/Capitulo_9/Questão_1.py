from itertools import combinations
from time import sleep
def main():
    bag_of_words=open("exemplos/words.txt")

    ###Function that returns if the word as any of the forbbiden letters
    def avoids(word,forbidden):
        for letter in word:
            if letter in forbidden:
                return False
        return True    
    ###Function that returns if the word have no letter "e"
    def has_no_e(word):
        return True if word.find("e")==-1 else False
    ### Ask the user to input the forbbiden letters
    def forbidden():
        answer="no"
        forbidden=[]
        while answer!="yes":
            answer=input(str("Digite uma letra para ser proibida conter nas palavras ou digite 'yes' para finalizar:\n"))
            if answer.lower() != "yes":
                forbidden.append(answer)
        return forbidden
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
            
    ### main function of the code
    def words(bag_of_words):
        fobidden_letters=forbidden()
        i=0
        j=0
        total=0
        for word in bag_of_words:
            if avoids(word,forbidden_letters) is True:
                i=i+1/8
            if has_no_e(word) is True:
                j=j+1
            total=total+1        
        return [i,j,total]
    less_affected=min_affected_words(bag_of_words)
    print("The 5 letters that exlude less words are: \n ",less_affected[0],"\n And they affect :",less_affected[1] )

    


if __name__=='__main__':
    main()