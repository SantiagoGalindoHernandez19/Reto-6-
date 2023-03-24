
def CantiadadDevolver(P: int, M:int, H:int, B:float):
    TOTAL = P*300+M*3300+H*350-B
    return TOTAL


if __name__ == "__main__":
    P= int(input("Ingrese la cantidad de panes(P): "))
    M= int(input("Ingrese la cantidad de leche (M): "))
    H= int(input("Ingrese la cantidad de huevos (H): "))
    B= int(input("Ingrese la cantidad de leche (B): "))

    resultado= CantiadadDevolver (P, M, H, B)
    print("El dinero a devolver o a deber es:  " + str(resultado))

   

