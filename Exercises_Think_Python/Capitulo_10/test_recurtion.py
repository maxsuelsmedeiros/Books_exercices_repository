def main():
    def fatorial(num):
        if num==1 or num==0:
            return 1
        else:
            print(num)
            return num * fatorial(num-1)
    def fibbonaci(num):
        if num<=1:
            return num
        else:
            return fibbonaci(num-1) + fibbonaci(num-2)
    x = int(input("Digite o valor para econtrar o fibbonaci"))
    res = fibbonaci(x-1)
    print("O valor de fibbonacci de %d é %d"%(x,res))

    
        
        
        

if __name__=='__main__':
    main()