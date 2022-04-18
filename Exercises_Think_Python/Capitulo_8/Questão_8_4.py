def main():
    def any_lowercase1(s):
        for c in s:
            if c.islower():
                return True
            else:
                return False
    
    '''
    any_lowercase1:
    Está correta, se qualquer letra for minuscula vai retornar True, caso não existem letras
    minusculas retorna False
    '''

    def any_lowercase2(s):
        for c in s:
            if 'c'.islower():
                return 'True'
            else:
                return 'False'

    '''
    any_lowercase2:
    Está errada por que o c entre aspas simples '' está dizendo que c não é uma variável e sim
    um caracter c e que é minusculo, a função sempre vai retornar True
    
    '''

    def any_lowercase3(s):
        for c in s:
            flag = c.islower()
        return flag

    '''
    any_lowercase3:
    Está errado, caso a última letra da string for maíuscula o returno ficara como False mesmo
    que as outras letras sejam minúsculas
    '''


    def any_lowercase4(s):
        flag = False
        for c in s:
            flag = flag or c.islower()
        return flag

    '''
    any_lowercase4:
    Está correto, se pelo menos uma for True, todas as outras igualdades do For vão continuar
    como True já que na lógica booleana True or qualquer coisa é True
    '''

    def any_lowercase5(s):
        for c in s:
            if not c.islower():
                return False
        return True
    '''
    any_lowercase5:
    Está errado, caso alguma letra não seja minúscula a função vai retornar False por conta do
    not c.islower(), mesmo que as primeiras letras sejam minúsculas caso a última seja maíuscula
    o retorno vai continuar como False
    '''

if __name__=='__main__':
    main()