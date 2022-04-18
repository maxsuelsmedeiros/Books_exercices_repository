def main():

    def bag():
        bag_of_words=open("/home/maxsuel/Documentos/pensePython/exemplos/words.txt")
        bag=bag_of_words.readlines()
        new_bag=[]
        for word in bag:
            word=word.rstrip('\n')
            new_bag.append(word)
        return new_bag
    
    def check_3(word,sequence):
        i=1
        while(i<len(word)):
            if word[i-1]==sequence[0] and word[i]==sequence[1] and i+5<=len(word):
                if word[i+1]==sequence[2] and word[i+2]==sequence[3] and word[i+3]==sequence[4] and word[i+4]==sequence[5]:
                    return True
            i=i+1
        return False
    
    def has_3_consec_dobles(bag_of_word):
        three_consec_doubles=[]
        for word in bag_of_word:
            check_doubles=[]
            i=1
            start=1
            while(i<len(word)):
                if word[i-1]==word[i]:
                    check_doubles.append(word[i-1])
                    check_doubles.append(word[i])
                i=i+1
            if len(check_doubles)==6:
                if check_3(word,check_doubles) is True:
                    three_consec_doubles.append(word)
        return three_consec_doubles

    

    print(has_3_consec_dobles(bag()))

    

if __name__=='__main__':
    main()