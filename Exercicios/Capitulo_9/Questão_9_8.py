def main():
    def palindrome_numbers():
        list_of_palindrome_numbers=[]
        for i in range(100000,1000000):
            comp_number=str(i)
            if comp_number[2:6:1]==comp_number[6:1:-1]:
                list_of_palindrome_numbers.append(i)
            elif comp_number[1:6:1]==comp_number[6:0:-1]:
                list_of_palindrome_numbers.append(i)
            elif comp_number[::1]==comp_number[::-1]:
                list_of_palindrome_numbers.append(i) 

        print(list_of_palindrome_numbers)
    palindrome_numbers()

if __name__=='__main__':
    main()