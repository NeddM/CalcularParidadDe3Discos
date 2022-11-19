def main():

    numeroDiscos = int(input("¿Cuantos díscos tiene tu RAID5?: "))

    if numeroDiscos < 4:
        print("Inserta un número válido de discos.")
    else:

        numeroDiscos -= 1
        disco = []
        paridad = []

        for bloque in range(numeroDiscos):
            disco.append(input(f"Inserta el bloque del disco {bloque}: "))

        for cifra in range(len(disco[1])):
            comparacion = 0
            for i in range(numeroDiscos):

                comparacion += int(disco[i][cifra])

            if comparacion % 2 == 0:
                paridad.append("0")
            elif comparacion % 2 == 1:
                paridad.append("1")

        for cifra in paridad:
            print(cifra, end="")


if __name__ == "__main__":
    main()
