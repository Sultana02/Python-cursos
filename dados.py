import random
print("Comencemos Juegos de Dados")
nombre1 = input("Jugador N° 1 ingrese su nombre: ")
nombre2= input("Jugador N° 2 ingrese su nombre: ")
jugador ="Si"

while jugador == "Si" or jugador == "si":
    player1=random.randint(1,6)
    player2=random.randint(1,6)
    print("----------------------------------------")
    print(nombre1,"(Jugador N° 1) Ha sacado: ",player1)
    print(nombre2,"(Jugador N° 2) Ha sacado: ",player2)
    print("-----------------------------------------")

    if player1 == player2:
        print("No hay ganadores, ¡Hay empate!")
        print("<<Juego Terminado>>")
    elif player1 > player2:
        print("Felicitaciones",nombre1,"..." "has ganado el juego!!")
        print("<<Juego Terminado>>")
    else: 
        print("Felicitaciones",nombre2,"..." "has ganado el juego!!")
        print("<<Juego Terminado>>")

    jugador = input("¿Desea comenzar una partida Nueva?\n" "Ingrese Si o No?: ")