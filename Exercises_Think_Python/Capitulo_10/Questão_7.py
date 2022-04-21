def main():
    def has_duplicates(t):
        count=0
        for i in t:
            for j in t:
                if j==i:
                    count+=1
            if count>1:
                return True
            count=0
        return False
    t=['a','b','c','e','d','h']
    print(has_duplicates(t))
if __name__=='__main__':
    main()