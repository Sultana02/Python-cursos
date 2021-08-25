print('TE DAMOS LA BIENVENIDA A RECICLASUPER')
inicio = True

while inicio:
    print('Ingrese importe a pagar: \n')
    importe = float(input("$: \n"))
    descuento = input('Código R-Rojo A-Amarillo B-Blanco \n')
    print(descuento)
    while (descuento != 'R') and(descuento != "A") and (descuento != "B"):
        descuento = str(input('Nuevamente Código R-Rojo A-Amarillo B-Blanco'))

    if descuento == 'R':
        total = importe - (40*importe/100)
    elif descuento == 'A':
        total = importe
    else: 
        total = importe - (25*importe/100)

    print('Debe pagar $', total)

    seguimos = input('Seguimos 1-SI 0-No')
    seguimos = int(seguimos)
    if seguimos == 0:
        inicio = False
print('FIN')