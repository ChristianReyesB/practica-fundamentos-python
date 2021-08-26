#Imprimir tu nombre
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")

#entero
edad = 25

#float
altura = 1.75

#convertir datos
edadString = str(edad)

print(edad + edad)
print(edadString + edadString)

print(type(edadString))

tuEdad = input("Introduce tu edad: ")
tuEdad = int(tuEdad)

#Estructura de control if
if tuEdad >= 18 and tuEdad < 200:
    print("Eres mayor de edad")
elif tuEdad >= 200:
    print("¿Eres inmortal?")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")

#Estructura de control for
for i in range(0,10):
    print(i)


