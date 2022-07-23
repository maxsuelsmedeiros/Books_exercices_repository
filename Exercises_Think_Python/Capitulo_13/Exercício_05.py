import random
def main():
    def histogram(s):
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        return d

    def choose_from_hist(hist_dictionary):
        hist=""
        for key,value in hist_dictionary.items():
            hist+=key*value
        letter_choose=random.choice(hist)
        return letter_choose,hist_dictionary[letter_choose]/sum(hist_dictionary.values())
    letter, probability = choose_from_hist(histogram(['a','a','b']))
    print("The choose letter as {} and the probability of that choice is {}".format(letter,probability))

if __name__=='__main__':
    main()