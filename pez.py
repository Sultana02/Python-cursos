pez = int(input("Ingrese tamaño del pez 1-Normal 2-Por debajo de lo normal 3-Por encima de lo normal 4-Sobredimensionado"))

if pez == 1:
    print("Pez en buenas condiciones")
elif pez == 2:
    print("Pez con problemas de nutrición")
elif pez == 3:
    print("Pez con sintomas de organismo contaminado")
else:
    print("Pez contaminado")

print("Terminamos")