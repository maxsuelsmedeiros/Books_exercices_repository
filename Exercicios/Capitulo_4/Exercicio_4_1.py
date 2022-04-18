import turtle
import math
def main():
    bob = turtle.Turtle()
    def polygon(t,length,n):

        for i in range(n):
            t.fd(length)
            t.lt(360/n)
#        turtle.mainloop()  
    def circle(t, r):
        circumference = 2 * math.pi * r
        n = 150
        length = circumference / n
        polygon(t,length,n)
    circle(bob,100)


if __name__ == "__main__":
    main()