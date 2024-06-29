import random
numero = random.randint(1,10)
print("¡Adivina el numero Random del 1 al 10!")
adivina=int(input("Ingresa un número: "))
while adivina<1 or adivina>10:
    print("No puedes ingresar numeros fuera del rango. Intentalo de nuevo")
    adivina=int(input("Ingresa un número: "))

while adivina != numero:
    if adivina != numero:
        print("Fallaste. Intentalo de nuevo")
        adivina=int(input("Ingresa un número: "))

print("Felicidades Adivinaste el número")