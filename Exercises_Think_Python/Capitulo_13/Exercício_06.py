import string
def main():
    #same code as in the book, to verify if the set operations are correct
    
    def process_file(filename):
        hist = dict()
        fp = open(filename)
        for line in fp:
            process_line(line, hist)
        return hist
    def process_line(line, hist):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    hist_emma = process_file('/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/emma.txt')
    set_emma=set(hist_emma.keys())
    #now reading the words that are considered valid in the english language
    words=open("/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/words.txt")
    bag_of_words=[]
    for word in words:
        bag_of_words.append(word.rstrip("\n"))
    set_words=set(bag_of_words)
    difference=set_emma.difference(set_words)
    print(difference)


if __name__=='__main__':
    main()