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
  [x, y] = input("Player 1 - Enter Location: ").split(",")
  x = int(x.strip())
  y = int(y.strip())
  if board[x][y] == " ":
    board[x][y] = letter1.upper()
  else:
    print("You cannot draw there!")
    player1()

def player2():
  [x, y] = input("Player 2 - Enter Location: ").split(",")
  x = int(x.strip())
  y = int(y.strip())
  if board[x][y] == " ":
    board[x][y] = letter2.upper()
  else:
    print("You cannot draw there!")
    player2()

def check_rows(symbol, player_name):
  for y in range(1, 5):
    # If the WHOLE row is filled, then you win.
    num_filled = 0
    for x in range(1, 5):
      if board[x][y] == symbol.upper():
        num_filled += 1
    if num_filled == 4:
      print(player_name + " has won the match!")
      return True

def check_columns(symbol, player_name):
  for x in range(1, 5):
    # If the WHOLE column is filled, then you win.
    num_filled = 0
    for y in range(1, 5):
      if board[x][y] == symbol.upper():
        num_filled += 1
    if num_filled == 4:
      print(player_name + " has won the match!")
      return True

def check_diagnol_1(symbol, player_name):
  num_filled = 0
  for i in range(1, 5):
    if board[i][i] == symbol.upper():
      num_filled += 1
  if num_filled == 4:
    print(player_name + " has won the match!")
    return True

def check_diagnol_2(symbol, player_name):
  num_filled = 0
  for i in range(1, 5):
    if board[i][5-i] == symbol.upper():
      num_filled += 1
  if num_filled == 4:
    print(player_name + " has won the match!")
    return True

def check_for_win():
  if check_rows(letter1, 'Player 1'):
    return True
  if check_rows(letter2, 'Player 2'):
    return True
  if check_columns(letter1, 'Player 1'):
    return True
  if check_columns(letter2, 'Player 2'):
    return True
  if check_diagnol_1(letter1, 'Player 1'):
    return True
  if check_diagnol_1(letter2, 'Player 2'):
    return True
  if check_diagnol_2(letter1, 'Player 1'):
    return True
  if check_diagnol_2(letter2, 'Player 2'):
    return True

while True:
  player1()
  printBoard()
  
  if check_for_win():
    break

  player2()
  printBoard()
  
  if check_for_win():
    break
