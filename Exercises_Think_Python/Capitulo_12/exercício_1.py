from re import X
from structshape import structshape


def main():
    def sumall(*args):
        return sum(args)
    print(sumall(1,2,3,4))
    t=((1,2,3),[4,5,6],{'a':7})
    print(structshape(t))


if __name__=='__main__':
    main()