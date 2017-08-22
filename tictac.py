matriz = [[' ' for x in range(3)] for x in range(3)]; player = 0

def printGrid():
	print('\n ' + str(matriz[0]) + '\n', str(matriz[1]) + '\n', str(matriz[2]) + '\n')
	checkVictory()

def makePlay(i, n):
	global player
	if matriz[i][n] != ' ':
		print('Jogada inválida.'); player -= 1
	else:
		matriz[i][n] = 'O' if player % 2 == 0 else 'X'
	printGrid()

def checkVictory():
	for mat in matriz:
		if all(i == 'X' for i in mat):
			print('Vitória do X.')
			exit()
		elif all(i == 'O' for i in mat):
			print('Vitória do O.')
			exit()
	for x in range(3):
		count = 0
		for y in range(3):
			if matriz[y][x] == 'X':
				count += 1
				if count == 3:
					print('Vitória do X.')
					exit()
			if matriz[y][x] == 'O':
				count += 1
				if count == 3:
					print('Vitória do O.')
					exit()

def main():
	global player; printGrid()
	while player < 9:
		try:
			if player % 2 == 0:
				play = str(input('1 > ')).split('x'); player += 1
				makePlay((int(play[0]) - 1), (int(play[1]) - 1))
			elif player % 2 != 0:
				play = str(input('2 > ')).split('x'); player += 1
				makePlay((int(play[0]) - 1), (int(play[1]) - 1))
		except ValueError as err:
			print('Valor inválido.'); play -= 1

main()
