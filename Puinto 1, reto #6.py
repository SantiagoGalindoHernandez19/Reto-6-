
from math import pi,sqrt
import math
pi = math.pi 
def AreayvolumenEsfe(r1:float)-> float:
    VE = (4/3)*pi*r1**3 # Volumen del la esfera 
    AC = (4*pi)*r1**2   # Area de la esfera 
    return VE,AC

def AreayVolumenCono(r2:float, h:float )-> float:
    VC = (1/3)*h*pi*(r2**2) # Volumen Cono
    AI = sqrt(r2**2) + (h**2) # Altura inclinada 
    AC = pi*r2(r2+AI)         # Area cono
    return VC, AI, AC

if __name__ == "__main__":
    r1=(float(input("Ingrese el radio de la esfera: ")))
    r2=(float(input("Ingrese el radio del cono: ")))
    h=(float(input("Ingrese la altura del cono ")))

    V = (r1, r2, h)
    A = (r1, r2, h)
    print("El volumen de la figura es " + str(V))
    print("El area de la figura es " + str(A))