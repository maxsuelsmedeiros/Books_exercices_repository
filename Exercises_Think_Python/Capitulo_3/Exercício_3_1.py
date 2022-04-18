def main():
    def right_justify(s):
        tamanho_espaço=70-len(s)
        for i in range(tamanho_espaço):
            print(" ", end="")
        print(s)
    right_justify("Yang")

if __name__ == '__main__':
    main()
