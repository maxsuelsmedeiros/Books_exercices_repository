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

    #Function to verify if the full word or the word with removed letters exist in the dictionary
    def it_exist(word,cmu_dict):
        if cmu_dict.get(word,-1) != -1:
            return True
        return False


    #Function developed by AllenDowney and used to answer this exercise
    def read_dictionary(filename='Exercises_Think_Python/c06d'):
        """Reads from a file and builds a dictionary that maps from
        each word to a string that describes its primary pronunciation.
        Secondary pronunciations are added to the dictionary with
        a number, in parentheses, at the end of the key, so the
        key for the second pronunciation of "abdominal" is "abdominal(2)".
        filename: string
        returns: map from string to pronunciation """
        d = dict()
        fin = open(filename)
        for line in fin:

            # skip over the comments
            if line[0] == '#': continue

            t = line.split()
            word = t[0].lower()
            pron = ' '.join(t[1:])
            d[word] = pron

        return d
    cmu_dictionary = read_dictionary()
    
    def verify_homophones(bag_of_words,cmu_list):
        list_of_homophones=[]
        for word in bag_of_words:
            #verify if the  word exist in the cmu dictionary and if it is bigger than 3, since need more than 3 letter to make a homophone
            if it_exist(word,cmu_list) is True and len(word)>=3:
                not_first_letter=word[1:]
                not_second_letter=word[:1]+word[2:]
                cmu_word=cmu_list[word]
                cmu_word_not_1=cmu_list.get(not_first_letter,-1)
                cmu_word_not_2=cmu_list.get(not_second_letter,-1)
                if cmu_word==cmu_word_not_1==cmu_word_not_2:
                    list_of_homophones.append([word,not_first_letter,not_second_letter,cmu_word])
        return list_of_homophones

    homophones_list=verify_homophones(bag_of_words,cmu_dictionary)
    print(homophones_list)

if __name__=='__main__':
    main()