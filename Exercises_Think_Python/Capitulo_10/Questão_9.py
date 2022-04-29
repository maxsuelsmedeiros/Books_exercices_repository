import time
def main():
    bag=open("Exercises_Think_Python/words.txt")
    bag=bag.readlines()
    #Function that removes the simple quotes and the \n from the words
    def remove_useless_simbols(bag):
        new_bag=[]
        for word in bag:
            word=word.strip("'")
            new_bag.append(word.strip("\n"))
        return new_bag
    bag_of_words=remove_useless_simbols(bag)
    #Function one that read the words from the file words and uses a list with append operation
    def append_operation(bag):
        new_bag=[]
        for word in bag:
            new_bag.append(word)
    #function that uses a list but uses the list = list + [value]
    def list_plus_element(bag):
        new_bag=[]
        for word in bag:
            new_bag = new_bag + [word]
    start_append=time.time()
    append_operation(bag)
    end_append=time.time()
    start_list_plus=time.time()
    list_plus_element(bag)
    end_list_plus=time.time()
    print("It took:",end_append-start_append,"seconds to finish the append function")
    print("It took:",end_list_plus-start_list_plus,"seconds to finish the list plus function")
    

if __name__=='__main__':
    main()