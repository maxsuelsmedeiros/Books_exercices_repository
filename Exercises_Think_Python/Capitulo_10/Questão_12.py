import bisect as bi
import time
def main():
    bag=open("Exercises_Think_Python/words.txt")
    def remove_useless_simbols(bag):
        new_bag=[]
        for word in bag:
            word=word.strip("'")
            new_bag.append(word.strip("\n"))
        return new_bag
    bag_of_words=remove_useless_simbols(bag)
    #Function that join words:
    def join_words(word1,word2):
        new_word=""
        word1=list(word1)
        word2=list(word2)
        count=0
        if len(word1)==len(word2):
            for letter in word1:
                new_word = new_word + word1[count] + word2[count]
                count+=1
        elif len(word1)>len(word2):
            for letter in word2:
                new_word = new_word + word1[count] + word2[count]
                count+=1
                for letter in range(len(word2),len(word1)):
                    new_word= new_word + word1[letter]
        else:
            for letter in word1:
                new_word = new_word + word1[count] + word2[count]
                count+=1
            for letter in range(len(word1),len(word2)):
                new_word= new_word + word2[letter]
        return new_word
    #Function that verify if the list is not empity
    def is_empty(t):
        if t == []:
            return True
        else:
            return False
    #Function that verify the existence of a word in a list faster then the IN operator
    def in_bisect(bag,word):
        position=bi.bisect_left(bag,word)
        if bag[position]==word:
            return position
        else:
            return "None"
    #This function joins 2 words and verify if the word exists
    def new_words(bag):
        new_word=""
        list_new_word=[]
    #Running through the list of words and then doing the same operation to verify if the words together make new valid words
        for i in bag:
            for j in bag:
                if j!=i:
                    new_word=join_words(i,j)
                    if in_bisect(bag,new_word) != "None":
                        list_new_word.append(new_word)
        return list_new_word
    print(new_words(bag_of_words))
    

if __name__=='__main__':
    main()