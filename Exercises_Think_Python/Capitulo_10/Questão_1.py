def main():
    ###This function recieves a list of lists of integer number and return the sum of ther
    def nested_sum(t):
        sum_list_elements=0
        for n in t:
            if type(n) is list:
                for i in n:
                    sum_list_elements += i
        return sum_list_elements
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))


if __name__=='__main__':
    main()