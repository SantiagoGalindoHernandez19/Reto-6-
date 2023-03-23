
def NumeroContagiados(D:int, c:int)->int:

    return  c * (D**2)

if __name__ == '__main__':
    D = int(input("Ingrese el numero de dias: "))
    C = int(input("Ingrese el numero de contagiados actuales: "))

total = NumeroContagiados(D,C)
print("El numero de contagiados despues de tantos dias es de " + str(total))
