import turtle
def main():
    bob = turtle.Turtle()
    def koch(t,length,n):
        if(n<=0):
            return
        else:
            t.lt(120)
            t.fd(length/3)
            t.lt(60)
            t.fd(length/3)
            t.rt(120)
            t.fd(length/3)
            t.lt(60)
            t.fd(length/3)
            koch(t,length,n-1)
    koch(bob,45,3)

if __name__ == "__main__":
    main()