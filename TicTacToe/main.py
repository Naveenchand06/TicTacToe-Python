

print('''
-----Welcome to TicTacToe-----

	 1 | 2 | 3
	---+---+---
	 4 | 5 | 6
	---+---+---
	 7 | 8 | 9
	''')

pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
elements = ['X', 'O', None]
total_turns = 1
turn = 'X'
is_on = True


while is_on:
	present = True
	while present:
		choice = int(input("Enter a position to put 'X' (1 - 9): "))
		if pos[choice - 1] in elements:
			pass
		elif choice <= 0 or choice > 9:
			print("Invalid choice")
		else:
			present = False

	pos[choice - 1] = turn

	print(' ' + pos[0] + ' | ' + pos[1] + ' | ' + pos[2])
	print("---+---+---")
	print(' ' + pos[3] + ' | ' + pos[4] + ' | ' + pos[5])
	print("---+---+---")
	print(' ' + pos[6] + ' | ' + pos[7] + ' | ' + pos[8])


	if (pos[0]==pos[1]==pos[2]==turn or pos[3]==pos[4]==pos[5]==turn or pos[6]==pos[7]==pos[8]==turn or
		pos[0]==pos[3]==pos[6]==turn or pos[1]==pos[4]==pos[7]==turn or pos[8]==pos[5]==pos[8]==turn or
		pos[0]==pos[4]==pos[8]==turn or pos[2]==pos[4]==pos[6]==turn):
		print(f"'{turn}' WON the game.")
		is_on = False

	

	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'


	total_turns += 1
	if total_turns > 9:
		print("----It's a DRAW----")
		is_on = False