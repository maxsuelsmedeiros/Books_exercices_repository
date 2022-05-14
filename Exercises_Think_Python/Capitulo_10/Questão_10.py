import math
import statistics
import bisect as bi
import time
def main():
    bag=open("Exercises_Think_Python/words_english.txt")
    def remove_useless_simbols(bag):
        new_bag=[]
        for word in bag:
            word=word.strip("'")
            new_bag.append(word.strip("\n"))
        return new_bag
    bag_of_words=remove_useless_simbols(bag)
    bag_of_words.sort()
    #function that searches for a word in the words file in a bisect way 
    def in_bisect(bag,word):
        position=bi.bisect_left(bag,word)
        if bag[position]==word:
            return position
        else:
            return "None"

    print("--------------------------------------------------------------")
    #Using recurtion to verify if the word exist in the file
    def in_bisect_recursive(bag,word):
        position=0
        if len(bag)==1 and word==bag[0]:
            position = 0
            return position
        elif len(bag)==1 and word!=bag[0]:
            return "None"
        else:
            if len(bag)%2==0:
                position=int(len(bag)/2)
            else:
                position=int(math.floor(len(bag)/2))
            if word==bag[position]:
                return position
            elif word<bag[position]:
                return in_bisect_recursive(bag[:position],word)
            else:
                return in_bisect_recursive(bag[position:],word)

    #function that takes half of the size each time but has a limit           
    def in_bisect_recursive_n_iterations(bag,word,countdown,position,minus,maximum):
        '''
        if (end+start)%2==0:
            position=int((end+start)/2)
        else:
            position=int(math.floor((end+start)/2))
        '''
        if bag[position]==word:
            return position
        elif countdown==0 and bag[position]!=word:
            return "None"
        else:
            '''
            if (end-start)%2==0:
                position=int((end-start)/2)
            else:
                position=int(math.floor((end-start)))
            '''
            if word<bag[position]:

                mediana=[]
                maximum=position
                for i in range(minus,maximum-1):
                    mediana.append(int(i))
                if len(mediana)>1:
                    position=int(statistics.median(mediana))
                else:
                    position=0
                return in_bisect_recursive_n_iterations(bag,word,countdown-1,position,minus,maximum)
            else:

                minus=position
                position=int(math.floor((position+maximum)/2))
                return in_bisect_recursive_n_iterations(bag,word,countdown-1,position,minus,maximum)
    
    
    #Function that verify if the middle of the list is even or odd           
    def is_odd_or_even(bag_of_words):
        position=0
        if len(bag_of_words)%2==0:
            position=len(bag_of_words)-1
            return position
        else:
            position=int(math.floor(len(bag_of_words)/2))
            return position
    #Function that counts the amount of times that the search function can go
    def count_div(bag):
        count=1
        tam=len(bag)
        while(tam>1):
            if tam%2==0:
                tam=int(tam/2)
                count+=1
            else:
                tam=int(math.floor(tam/2))
                count+=1
        return count
    start_function=time.time()
    bisect_operation=in_bisect(bag_of_words,"departed")
    end_function=time.time()
    print("The word 'departed' were found in the position {} using the bisect method, and took {} seconds to finish".format(bisect_operation,end_function-start_function))
    print("-------------------------------------------------".center(200))
    start_function=time.time()
    bisect_operation_recursive=in_bisect_recursive(bag_of_words,"departed")
    end_function=time.time()
    print("The word 'departed' were found in the position {} using the bisect method, and took {} seconds to finish".format(bisect_operation_recursive,end_function-start_function))
    print("++++++++++++++++++++++++++++++++++++++++++++++++".center(200))
    start_function=time.time()
    bisect_n_interations=in_bisect_recursive_n_iterations(bag_of_words,"departed",count_div(bag_of_words),is_odd_or_even(bag_of_words),0,len(bag_of_words)-1)
    end_function=time.time()
    print("The word 'departed' were found in the position {} using the bisect method, and took {} seconds to finish".format(bisect_n_interations,end_function-start_function))

if __name__=='__main__':
    main()