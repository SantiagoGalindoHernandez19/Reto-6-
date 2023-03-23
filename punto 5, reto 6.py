
def Interesprestamo(c: float, i: float, n:int)->float:
    tasadeinteres = (i * c) / 100
    return c * tasadeinteres**n

if __name__ == "__main__":
  c = int(input("Ingresar valor del prestamo(c): "))
  i = int(input("Ingresar porcentaje tasa de interes(i): "))
  n = int(input("Ingrese la cantidad de meses(n): "))

  total=Interesprestamo(c,i,n)
  print("El valor del prestamo es de " + str(total))

