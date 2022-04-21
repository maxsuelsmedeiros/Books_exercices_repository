import random
def main():
    def random_birthdays():
        list_of_days=[]
        for i in range(23):
            list_of_days.append(random.randint(1,365))
        return list_of_days
    def birthdays_same_day(t):
        students_same_birthday=[]
        for i in t:
            if t.count(i)>=2:
                students_same_birthday.append(t.index(i))
                students_same_birthday.append(t.index(i,i+1,len(t)-1))
        return students_same_birthday
    print(birthdays_same_day(random_birthdays()))



            
    

if __name__=='__main__':
    main()