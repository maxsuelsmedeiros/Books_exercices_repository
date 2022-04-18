import turtle
import math
import time

def main():
    bob = turtle.Turtle()

    def triangulo_interior(t,length):
        """Como todos os polígonos regulares formam um tringulo equilátero só é necessário
        criar esse triangulo e fazer a trilha para formar o escudo
        t : turtle
        length : é o tamanho do lado
        """
        for i in range(3):
            t.fd(length)
            print(length)
            t.rt(120)
        time.sleep(2)
    
    def escudo_poligonal(t, n, length):
        """ No caso de só desenhar um polígono essa função vai desenhar todas as linhas de 
        ligação
        t : turtle
        n : número de lados
        angle : é o angulo que a seta vai virar
        lenght : o tamanho do lado
        angle é criado na função

        """
        angle = 360.0/n
        for i in range(n):
            t.fd(length)
            print(length)
            t.rt(angle)
            print(angle)
            triangulo_interior(t,length)
    escudo_poligonal(bob,4,100)


if __name__ == "__main__":
    main()