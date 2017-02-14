board = {
  1: {
    1: " ",
    2: " ",
    3: " ",
    4: " "
  },
  2: {
    1: " ",
    2: " ",
    3: " ",
    4: " "
  },
  3: {
    1: " ",
    2: " ",
    3: " ",
    4: " "
  },
  4: {
    1: " ",
    2: " ",
    3: " ",
    4: " "
  },
}

print("Welcome to Tic Tac Toe. After each player has chosen their letter, they may choose where to put it, by giving coordinates seperated by a comma. Enjoy!\n\n")

letter1 = input("Player 1 - Choose letter(X/O): ")
if letter1.upper() == "X":
  letter2 = "O"
else:
  letter2 = "X"

def printBoard():
  for d in range(1, 5):
    print("\n---|---|---|---")
    for i in range(1, 5):
      if i == 4:
        print(" " + str(board[i][d]), end="")
      else:
        print(" " + str(board[i][d]) + " |", end="")
  print("\n"*2)
  
def player1():
  cmd = input("Player 1 - Enter Location: ").split(", ")
  if board[int(cmd[0])][int(cmd[1])] == " ":
    board[int(cmd[0])][int(cmd[1])] = letter1.upper()
  else:
    print("You cannot draw there!")
    player1()

def player2():
  cmd = input("Player 2 - Enter Location: ").split(", ")
  if board[int(cmd[0])][int(cmd[1])] == " ":
    board[int(cmd[0])][int(cmd[1])] = letter2.upper()
  else:
    print("You cannot draw there!")
    player2()

while True:
  player1()
  printBoard()
  
  if board[1][1] == letter1.upper() and board[2][1] == letter1.upper() and board[3][1] == letter1.upper() and board[4][1] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][2] == letter1.upper() and board[2][2] == letter1.upper() and board[3][2] == letter1.upper() and board[4][2] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][3] == letter1.upper() and board[2][3] == letter1.upper() and board[3][3] == letter1.upper() and board[4][3] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][4] == letter1.upper() and board[2][4] == letter1.upper() and board[3][4] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter1.upper() and board[1][2] == letter1.upper() and board[1][3] == letter1.upper() and board[1][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[2][1] == letter1.upper() and board[2][2] == letter1.upper() and board[2][3] == letter1.upper() and board[2][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[3][1] == letter1.upper() and board[3][2] == letter1.upper() and board[3][3] == letter1.upper() and board[3][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[4][1] == letter1.upper() and board[4][2] == letter1.upper() and board[4][3] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter1.upper() and board[2][2] == letter1.upper() and board[3][3] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[4][1] == letter1.upper() and board[3][2] == letter1.upper() and board[2][3] == letter1.upper() and board[1][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[2][1] == letter2.upper() and board[3][1] == letter2.upper() and board[4][1] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][2] == letter2.upper() and board[2][2] == letter2.upper() and board[3][2] == letter2.upper() and board[4][2] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][3] == letter2.upper() and board[2][3] == letter2.upper() and board[3][3] == letter2.upper() and board[4][3] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][4] == letter2.upper() and board[2][4] == letter2.upper() and board[3][4] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[1][2] == letter2.upper() and board[1][3] == letter2.upper() and board[1][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[2][1] == letter2.upper() and board[2][2] == letter2.upper() and board[2][3] == letter2.upper() and board[2][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[3][1] == letter2.upper() and board[3][2] == letter2.upper() and board[3][3] == letter2.upper() and board[3][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[4][1] == letter2.upper() and board[4][2] == letter2.upper() and board[4][3] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[2][2] == letter2.upper() and board[3][3] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[4][1] == letter2.upper() and board[3][2] == letter2.upper() and board[2][3] == letter2.upper() and board[1][4] == letter2.upper():
    print("Player 2 has won the match!")
    break

  player2()
  printBoard()
  
  if board[1][1] == letter1.upper() and board[2][1] == letter1.upper() and board[3][1] == letter1.upper() and board[4][1] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][2] == letter1.upper() and board[2][2] == letter1.upper() and board[3][2] == letter1.upper() and board[4][2] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][3] == letter1.upper() and board[2][3] == letter1.upper() and board[3][3] == letter1.upper() and board[4][3] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][4] == letter1.upper() and board[2][4] == letter1.upper() and board[3][4] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter1.upper() and board[1][2] == letter1.upper() and board[1][3] == letter1.upper() and board[1][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[2][1] == letter1.upper() and board[2][2] == letter1.upper() and board[2][3] == letter1.upper() and board[2][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[3][1] == letter1.upper() and board[3][2] == letter1.upper() and board[3][3] == letter1.upper() and board[3][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[4][1] == letter1.upper() and board[4][2] == letter1.upper() and board[4][3] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter1.upper() and board[2][2] == letter1.upper() and board[3][3] == letter1.upper() and board[4][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[4][1] == letter1.upper() and board[3][2] == letter1.upper() and board[2][3] == letter1.upper() and board[1][4] == letter1.upper():
    print("Player 1 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[2][1] == letter2.upper() and board[3][1] == letter2.upper() and board[4][1] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][2] == letter2.upper() and board[2][2] == letter2.upper() and board[3][2] == letter2.upper() and board[4][2] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][3] == letter2.upper() and board[2][3] == letter2.upper() and board[3][3] == letter2.upper() and board[4][3] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][4] == letter2.upper() and board[2][4] == letter2.upper() and board[3][4] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[1][2] == letter2.upper() and board[1][3] == letter2.upper() and board[1][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[2][1] == letter2.upper() and board[2][2] == letter2.upper() and board[2][3] == letter2.upper() and board[2][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[3][1] == letter2.upper() and board[3][2] == letter2.upper() and board[3][3] == letter2.upper() and board[3][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[4][1] == letter2.upper() and board[4][2] == letter2.upper() and board[4][3] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[1][1] == letter2.upper() and board[2][2] == letter2.upper() and board[3][3] == letter2.upper() and board[4][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
  elif board[4][1] == letter2.upper() and board[3][2] == letter2.upper() and board[2][3] == letter2.upper() and board[1][4] == letter2.upper():
    print("Player 2 has won the match!")
    break
