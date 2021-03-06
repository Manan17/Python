board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
winner = None
game_still_on = True
current_player = "X"
def display_board():
  global board
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

  
def handle_turn(player):
  global board
  number = input('Enter the number from 1-9 : ')
  valid = False
  while not valid:
    while number not in ["1","2","3","4","5","6","7","8","9"]:
      number = input('Enter the number from 1-9 : ')

    number = int(number)
    if board[number-1] == "-":
      valid = True

    else:
      print("You cannot go there")
      
  board[number-1] = player
  display_board()
  
def check_game_over():
  global game_still_on
  check_winner()
  check_tie()
  
def check_winner():
  global winner 
  row_winner = check_rows()
  col_winner = check_col()
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
    
  elif col_winner:
    winner = col_winner
   
  elif diagonal_winner:
    winner = diagonal_winner
   
  else:
    winner = None
     
  
  
def check_rows():
  global board
  global game_still_on
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_on = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None
  
  
    
    
def check_col():
  global board
  global game_still_on
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  
  if col_1 or col_2 or col_3:
    game_still_on = False
    
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  else:
     return None

  
def check_diagonals():
  global game_still_on
  dia_1 = board[0] == board[4] == board[8] != "-"
  dia_2 = board[2] == board[4] == board[6] != "-"
  
  if dia_1 or dia_2:
    game_still_on = False
    
  if dia_1:
    return dia_1
  elif dia_2:
    return dia_2
  else:
    return None


def check_tie():
  global game_still_going
  global board
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False
  
def flip_turn():
  global current_player  
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  
def play_game():
  display_board()
  global game_still_on

  while game_still_on:
    handle_turn(current_player)
    check_game_over()
    flip_turn()

  if winner == "X" or winner == "O":
    print(winner + " is the winner") 
  elif winner == None:
    print("TIE")
    
  
play_game()
