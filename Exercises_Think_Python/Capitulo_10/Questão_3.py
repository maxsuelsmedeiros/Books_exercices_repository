def main():
    def middle(t):
        t.pop(0)
        t.pop(len(t)-1)
        return t
    t = [-1,0.5,1,2,3,4,8]
    print(middle(t))

if __name__=='__main__':
    main()