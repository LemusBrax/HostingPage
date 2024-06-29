import math
print("Este programa calcula el valor de una raíz")
val1=float(input("Ingresa el valor que se desea calcular: "))
while val1<0:
    print("No se pueden ingresar números negativos. Inténtalo de nuevo.")
    val1=float(input("Ingresa el valor que se desea calcular: "))

val1=math.sqrt(val1)
print("El resultado es {0:.2f}" .format(val1))