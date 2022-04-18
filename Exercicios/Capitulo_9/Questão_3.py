def main():
    def avoids(word,forbidden):
        for letter in word:
            if letter in forbidden:
                return False
        return True
    print(avoids("piranha",["e","w","q"]))

if __name__=='__main__':
    main()