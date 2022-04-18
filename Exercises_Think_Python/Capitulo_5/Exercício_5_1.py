import time as t
def main():
    '''
    Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e 
    segundos, mais o número de dias desde a época.
    '''
    def converter_tempo_atual(time):
        """
        Função para converter o tempo desde a Epoch para horas,minutos e segundos
        time : hora que o sistema retorna
        """
        tempo_horas=int(time//3600)
        tempo_minutos=int(time//60)
        tempo_segundos=int(time)
        tempo_dias=int(tempo_horas//24)
        print("Se passaram em dias desde do Epoch: " , tempo_dias)
        print("Se passaram em horas: ",tempo_horas)
        print("Se passaram em minutos: ",tempo_minutos)
        print("Se passaram em segundos: ",tempo_segundos)
        print("Se passaram em anos:",int(tempo_dias//365))


    converter_tempo_atual(t.time())
if __name__ == "__main__":
    main()
