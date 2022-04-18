def main():
    def age_palindrome():
        mother_age=36
        son_age=0
        palindrome_ages_son=[]
        palindrome_ages_mother=[]
        while son_age<300:
            str_son_age=str(son_age)
            str_mother_age=str(mother_age)
            if son_age<10:
                str_son_age=str(str_son_age).zfill(2)
            elif mother_age>=100:
                str_son_age=str(str_son_age).zfill(3)
            if str_son_age[::1]==str_mother_age[::-1]:
                palindrome_ages_son.append(str_son_age)
                palindrome_ages_mother.append(str_mother_age)
            son_age=son_age+1
            mother_age=mother_age+1
        return palindrome_ages_son,palindrome_ages_mother
    son,mother=age_palindrome()
    print("The son age is: ",son[5])
        


if __name__=='__main__':
    main()