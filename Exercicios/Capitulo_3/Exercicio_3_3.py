def main():

    def desenhar_linhas():
        print("+ - - - - + - - - - +")
    def desenhar_coluna():
        print("|         |         |")
    def desenhar_grade():
        desenhar_linhas()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_linhas()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_coluna()
        desenhar_linhas()
    #Desenhar a grade extra
    

    desenhar_grade()
if __name__ == "__main__":
    main()