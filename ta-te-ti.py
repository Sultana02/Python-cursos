def imprimir_tablero(Tablero):
	for fila in Tablero:
		for i in range(len(fila)):
			if i == len(fila) - 1:
				print(fila[i], end='\n')
			else:
				print(fila[i], end='  ')

def cambiar_tablero(Tablero, posicion, player):
	if player:
		simbology = 'X'
	else:
		simbology = 'O'

	if posicion == 1:
		if Tablero[2][0] == ' ':
			Tablero[2][0] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 2:
		if Tablero[2][2] == ' ':
			Tablero[2][2] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 3:
		if Tablero[2][4] == ' ':
			Tablero[2][4] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 4:
		if Tablero[1][0] == ' ':
			Tablero[1][0] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 5:
		if Tablero[1][2] == ' ':
			Tablero[1][2] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 6:
		if Tablero[1][4] == ' ':
			Tablero[1][4] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 7:
		if Tablero[0][0] == ' ':
			Tablero[0][0] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 8:
		if Tablero[0][2] == ' ':
			Tablero[0][2] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	elif posicion == 9:
		if Tablero[0][4] == ' ':
			Tablero[0][4] = simbology
			return 0
		else:
			return 'La posicion se encuentra ocupada, ingrese otra posicion... '
	else:
		return 'Esa posicion no existe!!!'



def un_ganador(Tablero):
	for simbology in ['X', 'O']:
		fila_0 = Tablero[0][0] == simbology and Tablero[0][2] == simbology and Tablero[0][4] == simbology
		fila_1 = Tablero[1][0] == simbology and Tablero[1][2] == simbology and Tablero[1][4] == simbology
		fila_2 = Tablero[2][0] == simbology and Tablero[2][2] == simbology and Tablero[2][4] == simbology
		colum_0 = Tablero[0][0] == simbology and Tablero[1][0] == simbology and Tablero[2][0] == simbology
		colum_1 = Tablero[0][2] == simbology and Tablero[1][2] == simbology and Tablero[2][2] == simbology
		colum_2 = Tablero[0][4] == simbology and Tablero[1][4] == simbology and Tablero[2][4] == simbology
		diag_abajo = Tablero[0][0] == simbology and Tablero[1][2] == simbology and Tablero[2][4]== simbology
		diag_arriba= Tablero[2][0] == simbology and Tablero[1][2] == simbology and Tablero[0][4]== simbology
		

		if fila_0 or fila_1 or fila_2 or colum_0 or colum_1 or colum_2 or diag_abajo or diag_arriba:
			if simbology == 'X':
				return 1
			elif simbology == 'O':
				return 2
			break


Tablero = [
	[' ','|',' ','|',' '],
	[' ','|',' ','|',' '],
	[' ','|',' ','|',' '],
]
imprimir_tablero(Tablero)

Turno1 = True
player1 = ' '
player2= ' '
Turno = 0
imprimir_tablero(Tablero)

while Turno < 9:
	if player1 == ' ':
		print('Nombre del Jugador Nro 1 (X): ')
		player1 = input()
		print('Nombre del Jugador Nro 2 (O): ')
		player2 = input()
	else:
		if Turno1:
			print(player1 +' ' + 'Elija una posicion en el Tablero: ')
		else:
			print(player2 +' ' + 'Elija una posicion en el Tablero: ')

		jugada = int(input())

		capacidad = cambiar_tablero(Tablero, jugada, Turno1)
		if capacidad == 0:
			Turno1 = not Turno1
			Turno += 1
			imprimir_tablero(Tablero)
			if un_ganador(Tablero) == 1:
				print(player1 +' '+ "Felicidades!!... Ha ganado esta partida!")
				break
			elif un_ganador(Tablero) == 2:
				print(player2+' ' + "Felicidades!!... Ha ganado esta partida!")
				break
		else: 
			print(capacidad)
		if Turno == 9:
			print("Nadie ha Ganado,(Empate) ...Juego Terminado!")
