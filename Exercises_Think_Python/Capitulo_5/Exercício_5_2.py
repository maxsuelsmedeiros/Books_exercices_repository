def main():
    def check_fermat(a,b,c,n):
        """
        Função para testar se o último teorema de Fermat é verdadeiro, o teorema diz:
        "não existem números inteiros a, b e c tais que a**n + b**n == c**n para 
        quaisquer valores de n maiores que 2"
        A função vai receber 4 variáveis, testar elas e usar condicional IF para testar
        a : valor inteiro
        b : valor inteiro
        c : valor inteiro
        n : valor inteiro que será o expoente
        """
        if (n>2 and a**n + b**n == c**n ):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
    def try_fermat():
        """
        Função simples feita para receber valores do usuário e converter em inteiro para 
        testar a função de Fermat
        """
        valor_a=int(input("Digite um valor inteiro:\n"))
        valor_b=int(input("Digite um valor inteiro:\n"))
        valor_c=int(input("Digite um valor inteiro:\n"))
        valor_n=int(input("Digite um valor inteiro maior do que 2:\n"))
        check_fermat(valor_a,valor_b,valor_c,valor_n)
    try_fermat()
if __name__== "__main__":
    main()
