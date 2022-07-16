# from dis import _HaveCodeOrStringType
from turtle import width
from more_itertools import unzip
import unidecode
import re
from matplotlib import pyplot as plt
def main():
    #take the lines from the file and them return it
    def organize_the_text(path):
        with open("/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/language_samples.txt") as language:
            samples=language.readlines()
            for index,line in enumerate(samples):
                samples[index]=line.rstrip("\n")

        return samples
    #Function that verify the frequency of the letters in a string
    def most_frequent(text):
        t=dict()
        for language_text in text:
            key_values=language_text.split("->")
            temp=unidecode.unidecode(key_values[1])
            temp=re.sub(r'[^\w\s]','',temp)
            temp=temp.replace(" ","")
            temp=temp.lower()
            temp_dict=dict()
            for letter in temp:
                temp_dict[letter]=temp_dict.get(letter,0)+1
            #keep this to take the language as a key and next the descentend letters as values
            t[key_values[0]]=sorted(temp_dict.items(),reverse=True)
        tuple_dict=()
        tuple_dict=zip(t.items())
            
        return t
    path_sample1="/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/language_samples.txt"
    path_sample2="/home/maxssdlinux/Documentos/Books_exercices_repository/Exercises_Think_Python/emma.txt"
    sample_language=organize_the_text(path_sample1)
    main_letters_per_language=most_frequent(sample_language)
    for language,letters in main_letters_per_language.items():
        print(language,letters)
        print("+++++++++++++++++++++++++++++++++++++++++++".center(100))
    

if __name__=='__main__':
    main()