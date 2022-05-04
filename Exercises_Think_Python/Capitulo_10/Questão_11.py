def main():
    bag=open("Exercises_Think_Python/words.txt")
    def remove_useless_simbols(bag):
        new_bag=[]
        for word in bag:
            word=word.strip("'")
            new_bag.append(word.strip("\n"))
        return new_bag
    bag_of_words=remove_useless_simbols(bag)
    #Function that verify if the word is the inverse of other
    def is_oposite(word,oposite):
        return True if word==oposite[::-1] else False
    #Function that returns all the inverse pair of words in the words file
    def inverse_pairs(bag):
        position=0
        inverse_list=[]
        for i in bag:
            if i[::-1] in bag:
                position=bag.index(i[::-1])
                inverse_list.append(i+"+"+bag[position])
        return inverse_list
    print(inverse_pairs(bag_of_words))

    

if __name__=='__main__':
    main()