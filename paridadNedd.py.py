cifra1 = input("Inserta el primer numero: ")
cifra2 = input("Inserta el segundo numero: ")
cifra3 = input("Inserta el tercer numero: ")

paridad = []

for cifra in range(len(cifra1)):
    comparacion = int(cifra1[cifra]) + \
        int(cifra2[cifra]) + int(cifra3[cifra])
    
    if comparacion % 2 == 0:
        paridad.append("0")
    elif comparacion % 2 == 1:
        paridad.append("1")

for cifra in paridad:
    print(cifra, end="")
