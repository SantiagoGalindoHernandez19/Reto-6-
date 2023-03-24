
a = int(input("Ingresa el primer numero: ")) 
b = int(input("Ingresa el segundo numero: ")) 
c = int(input("Ingresa el tercer numero: "))
d = int(input("Ingresa el cuarto numero "))
e = int(input("Ingresa el quinto numero ")) 

def promedio(a:int, b:int, c:int, d:int, e:int)->int: 
    return (a+b+c+d+e)/5


total= promedio(a,b,c,d,e)
print("El promedio de los numeros es " + str(total))


lst = [a,b,c,d,e] 

def median(l):
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]

print("La mediana de la lista de numeros es ", median(lst))

multi = (a*b*c*d*e)



from math import sqrt
def multiplicacion(a:int, b:int, c:int, d:int, e:int)->int: 
    multi = (a*b*c*d*e)
    return sqrt (multi)
    
resultado=multiplicacion(a,b,c,d,e)
print("El promedio multiplicativo es ",resultado)


Lista = [a,b,c,d,e]
for recorrido in range(1,len(Lista)):
      for posicion in range(len(Lista) - recorrido):
           if Lista [posicion] > Lista [posicion +1 ]:
            temp = Lista [posicion]
            Lista[posicion] = Lista[posicion + 1]
            Lista[posicion + 1] = temp

print ("Numeros de forma ascendente ",Lista)

for recorrido in range(1,len(Lista)):
    for posicion in range(len(Lista) - recorrido):
        if Lista [posicion] < Lista [posicion +1 ]:
            temp = Lista [posicion]
            Lista[posicion] = Lista[posicion + 1]
            Lista[posicion + 1] = temp

print ("Numeros de forma descendente ",Lista)


lista = [a,b,c,d,e]
alto = lista [0]

for i in range (0,len(lista)):
    if lista[i] > alto:
        alto = lista[i]
print("El numero mayor es: ", alto)

lista = [a,b,c,d,e]
bajo = lista [0]

for i in range (0,len(lista)):
    if lista[i] < bajo:
        bajo = lista[i]
print("El numero menor es: ", bajo)

resultado = (alto**bajo)
print("La potencia es: ", resultado)

raiz = bajo**(1/3) 
print("La raiz cubica del numero menor es", raiz)


           