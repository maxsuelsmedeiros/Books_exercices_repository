def main():
    s="Hello"
    n = 2
    def print_n(s, n):
        if n <= 0:
            return
        print(s)

    def diagrama_de_pilha():
        print("__main__", end=" ")
        print(" | s ---->",s)
        for i in range(len("__main__ ")):
            print(" ", end="")
        print(" | n ---->",n)
    def _n(palavra,n):
        if n<=0:
            return
        else:
            letra=palavra[n-1]
            print(letra)
            _n(palavra,n-1)
            print(n)
    _n("Yang",len("Yang"))


    diagrama_de_pilha()
if __name__ == "__main__":
    main()