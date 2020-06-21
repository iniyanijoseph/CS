board = [["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"] ]


def printboard():
	for row in board:
		# change below to a for loop
		print(row[0] + " " + row[1] + " " + row[2] + " " + row[3])
	print()
		
def checkwin():
	for i in [0,1,2,3]:
		# change conditions to loop
		if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2]==board[i][3] and board[i][0] != "_":
			return board[i][0]
		if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i]==board[3][i] and board [0][i] != "_":
			return board[0][i]
	if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==board[3][3] and board[0][0]!="_":
		return board[0][0]
	if board[0][3]==board[1][2] and board[1][2]==board[2][1] and board[2][1]==board[3][0] and board[0][3]!="_":
		return board[0][3]	
	return "_"
printboard()
y="X"
a=0
while True:
	
	position=input("Coordinates?")
	x = position.split()
	if board[int(x[0])][int(x[1])] != "X" and "O" != board[int(x[0])][int(x[1])]:
		a=a+1
		board[int(x[0])][int(x[1])]=y
	else:
		print("Choose different space")
	printboard()
	z=checkwin()
	if z=="X" or z=="O":
		print("Congrats! " + z + " is win.")
		break 
	if a==16:
		print("Draw")
		break
	
	if y=="X":
		y="O"
	else:
		y="X"
		
