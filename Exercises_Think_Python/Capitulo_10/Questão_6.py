import itertools as iTools
def main():
    def is_anagram(word1,word2):
        compare_anagram=list(word1)
        compare_anagram=list(iTools.permutations(compare_anagram))
        for i in compare_anagram:
            i=''.join(i)
            if i==word2:
                return True
        return False
    word1="alegria"
    word2="regalia"
    print(is_anagram(word1,word2))

if __name__=='__main__':
    main()