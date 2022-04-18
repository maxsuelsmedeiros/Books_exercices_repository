def main():
    print("__main__ ----->")
    """
    Essa função faz a recursividade e quando chega a zero par e exibe a soma dos valores 
    que foram somados durante os ciclos de recursividade, IMPORTANTE o valor de n SÓ PODE
    SER UM INTEIRO POSITIVO, caso seja um float ou inteiro negativo a função será recursiva
    eterna

    n : contador
    s : valor da soma do contador
    """

    def recurse(n, s):
        if n == 0:
            print("        ----->",end="")
            print(s)
        else:
            recurse(n-1, n+s)
    print("recurse ", end="")
    recurse(3, 0)


if __name__ == "__main__":
    main()
