import turtle
def main():
    bob = turtle.Turtle()
    print(bob)
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
    turtle.mainloop()
    


if __name__ == "__main__":
    main()