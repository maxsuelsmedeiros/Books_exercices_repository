def main():
    #This function sum the keys that repeat them selfs and add that number as their value
    def histogram(s):
        d = dict()
        for c in s:
            d[c]=d.get(c,0)+1
        return d
    #This function sort the dictionary and print their values
    def print_hist(h):
        for key in sorted(h):
            print(key,h[key])
    print_hist(histogram("paralelepipedo"))
    
    def fibonacci(n):
        known = {0:0, 1:1}
        if n in known:
            return known[n]
        res = fibonacci(n-1) + fibonacci(n-2)
        known[n] = res
        return res
    print("################################".center(50))
    known={'a':1,'b':2}
    print(known)
    def test_global():
        known['c'] = 3
    test_global()
    print(known)

if __name__=='__main__':
    main()