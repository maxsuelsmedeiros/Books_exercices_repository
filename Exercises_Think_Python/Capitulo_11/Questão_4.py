def main():
    def dict_has_duplicates(list_of_values):
        dict_list={}
        for letter in list_of_values:
            if dict_list.get(letter,0) > 0:
                return False
            else:
                dict_list[letter]=dict_list.get(letter,0)+1
        return True
    eg="twelve"
    print(dict_has_duplicates(list(eg)))

if __name__=='__main__':
    main()