def main():
    def has_no_e(word):
        return True if word.find("e")==-1 else False
    print(has_no_e("atlanta"))


if __name__=='__main__':
    main()