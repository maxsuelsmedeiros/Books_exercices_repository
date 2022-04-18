def main():
    #Exercicio 2.2 - 1
    r=5
    pi=3.14159
    volume_esfera=(4/3)*pi*r**3
    print(volume_esfera)
    #Exercicio 2.2 - 2
    custo_transporte_inicial=3.00
    custo_transporte=0.75
    preço_de_capa=24.95
    custo_total=((preço_de_capa/0.4)-preço_de_capa)*60+((59*custo_transporte)+custo_transporte_inicial)
    print("Custo de atacado para as 60 cópias",custo_total,"$")
    #Exercício 2.2 - 3 16.30 + 21.36
    tempo = (8.15*2)+(7.12*3)
    t1 = (8*60)*2+30
    t2 = (7*60)*3+36
    t_total = (t1+t2)/60
    print(t_total)
    print((((6*60)+52)+t_total))





    

if __name__== '__main__':
    main()