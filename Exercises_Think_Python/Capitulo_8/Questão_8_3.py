def main():
    def is_palindrome(word):
        i = 0
        j = len(word)-1
        while i<j:
            if word[i] != word[j]:
                return False
            i = i+1
            j = j-1
        return True
    def one_line_palindrome(palavra):
        return True if palavra[::1]==palavra[::-1] else False

    print(is_palindrome("omissíssimo"))
    print(one_line_palindrome("omissíssimo"))



if __name__=='__main__':
    main()