def main():
    def is_sorted(t):
        return True if sorted(t)==t else False
    t=[4,2,3]
    t2=["a","b","c"]
    print(is_sorted(t))
    print(is_sorted(t2))

if __name__=='__main__':
    main()