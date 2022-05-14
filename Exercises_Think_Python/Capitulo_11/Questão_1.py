import time
def main():
    bag=open("Exercises_Think_Python/words.txt",'r')
    bag=bag.readlines()
    #function that reads the words in the words file and use them as keys for the dictionary
    def file_to_dict(bag,word_to_search):
        words_dict={}
        for word in bag:
            word= str(word)
            words_dict[word.rstrip("\n")]=len(word.rstrip("\n"))
        start_in=time.time()
        if word_to_search in words_dict.keys():
            end_in=time.time()
            print("+++++++++++++++++++++++++++LOOK it took:\n{}\n+++++++++++++++++++++++++++".format(end_in-start_in))
            return words_dict,True
        else:
            return words_dict,False
    
    dict_from_words,exists=file_to_dict(bag,"clear")
    print("It is {} that the word informed exists in the dict and the dict itself is\n {}".format(exists,list(dict_from_words.items())[0:10]))

    
if __name__=='__main__':
    main()