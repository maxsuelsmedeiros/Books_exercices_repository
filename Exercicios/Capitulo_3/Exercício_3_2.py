def main():
    def print_twice(bruce):
        print(bruce)
        print(bruce)
    def print_spam():
        print('spam')
    def do_twice(f,x):
        f(x)
        f(x)
    def do_four(p,y):
        p(y)
        p(y)

    do_four((print_twice,"três")

if __name__ == "__main__":
    main()
