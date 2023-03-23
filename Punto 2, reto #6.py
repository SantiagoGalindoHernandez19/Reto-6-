
from math import pi
import math
pi = math.pi 

def AreayperimetroRec(b:float, a:float, )-> float:
    AR = (a*b)          # Area rectangulo
    PR = (2*b)+(2*a)    # Permietro rectangulo
    return AR, PR

def AreayperimetroCir(r:float)-> float:
    AC = pi*(r**2)      # Area Circulo    
    PC = 2*pi*r         # Perimetro Circulo
    return AC, PC

if __name__ == "__main__":
    a = float(input("Ingrese el ancho del rectang5ulo (a): "))
    b = float(input("Ingrese el largo del rectangulo (b): "))
    r = float(input("Ingrese radio del circulo (r): "))

    rec= AreayperimetroRec(b,a)
    Cir= AreayperimetroCir(r)
    print("El perimetro y area del rectangulo es " + str(rec))
    print("El perimetro y area del circulo es " + str(Cir))