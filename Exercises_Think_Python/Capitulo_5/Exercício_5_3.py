def main():
    def is_triangle(lado_1,lado_2,lado_3):
        """
        Função simples que recebe três (03) números inteiros e verifica se a soma dos dois
        (02) valores menores é igual ou maior que o maior
        lado_1 : valor do comprimento do lado
        lado_2 : valor do comprimento do lado
        lado_3 : valor do comprimento do lado
        """
        if (lado_1>lado_2 and lado_1>lado_3):
            if(lado_2+lado_3>=lado_1):
                print("Yes")
            else:
                print("No")
        elif (lado_2>lado_1 and lado_2>lado_3):
            if (lado_1+lado_3>=lado_2):
                print("Yes")
            else:
                print("No")
        elif (lado_3>lado_1 and lado_3>lado_2):
            if (lado_1+lado_2>=lado_3):
                print("Yes")
            else:
                print("No")
        elif (lado_1==lado_2 or lado_1 == lado_3 or lado_2==lado_3):
            print("Yes")
    def try_is_triangle():
        """
        Função simples que solicita ao usuário que digite três (03) valores para os 
        lados e então converte-lôs para inteiro 
        """
        valor_l_1=float(input("Digite por favor o primeiro valor para o lado:\n"))
        valor_l_1=int(valor_l_1)
        valor_l_2=float(input("Digite por favor o segundo valor para o lado:\n"))
        valor_l_2=int(valor_l_2)
        valor_l_3=float(input("Digite por favor o terceiro valor para o lado:\n"))
        valor_l_3=int(valor_l_3)
        is_triangle(valor_l_1,valor_l_2,valor_l_3)
    try_is_triangle()



if __name__ == "__main__":
    main()