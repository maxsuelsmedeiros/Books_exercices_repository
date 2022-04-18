def print_twice(bruce):
    print(bruce)
    print(bruce)
def print_spam():
    print('spam')
def do_twice(f,x):
    f(x)
    f(x)
def do_four(p,y):
    print_twice(y)
    print_twice(y)

do_four(do_twice,"três")