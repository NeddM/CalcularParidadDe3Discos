def main():

    print("""
   _____      _            _                          _     _           _ 
  / ____|    | |          | |                        (_)   | |         | |
 | |     __ _| | ___ _   _| | ___    _ __   __ _ _ __ _  __| | __ _  __| |
 | |    / _` | |/ __| | | | |/ _ \\  | '_ \\ / _` | '__| |/ _` |/ _` |/ _` |
 | |___| (_| | | (__| |_| | | (_) | | |_) | (_| | |  | | (_| | (_| | (_| |
  \\_____\\__,_|_|\\___|\\__,_|_|\\___/  | .__/ \\__,_|_|  |_|\\__,_|\\__,_|\\__,_|
                                    | |                                   
                                    |_|                                   
               _____           _____ _____    _____                       
              |  __ \\    /\\   |_   _|  __ \\  | ____|                      
              | |__) |  /  \\    | | | |  | | | |__                        
              |  _  /  / /\\ \\   | | | |  | | |___ \\                       
              | | \\ \\ / ____ \\ _| |_| |__| |  ___) |                      
              |_|  \\_/_/    \\_|_____|_____/  |____/                       
                                                                          
                https://www.github.com/NeddM                                                          
    """)

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
            for discos in range(numeroDiscos):

                comparacion += int(disco[discos][cifra])

            if comparacion % 2 == 0:
                paridad.append("0")
            elif comparacion % 2 == 1:
                paridad.append("1")

        print("El bloque de paridad es: ", end="")
        for cifra in paridad:
            print(cifra, end="")


if __name__ == "__main__":
    main()
