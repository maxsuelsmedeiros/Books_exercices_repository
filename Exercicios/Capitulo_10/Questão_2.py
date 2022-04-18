def main():
    def cumsum(t):
        last_digit=0
        cumulative=[]
        for n in t:
            cumulative.append(n+last_digit)
            last_digit += n
        return cumulative
        

    t = [5,2,8,10]
    print(cumsum(t))

if __name__=='__main__':
    main()