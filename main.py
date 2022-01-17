board = [
  "-", "-", "-", 
  "-", "-", "-", 
  "-", "-", "-"]

player = "X"


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def get_player_move(player):
  print("\nPlayer " + player)
  while True:
    move = get_input()
    if check_position(move):
      break
    else:
      print("Invalid move, try again.")
  return move


def get_input():
  while True:
    string = input("Please input your move (1-9): ")
    try:
      move = int(string)
      if move >= 1 and move <= 9:
        return move-1
    except:
      pass


def check_position(position):
  # return true if position is empty, false otherwise
  return board[position] == "-"


def update_board_with_symbol_at_position(symbol, position):
  board[position] = symbol


def switch_player():
  global player
  if player == "X":
    player = "O"
  else:
    player = "X"


def check_win():
  return check_vertical() or check_horizontal() or check_diagonal()


def check_vertical():
  if board[0] != "-":
    if board[0] == board[3] == board[6]:
      return True
  if board[1] != "-":
    if board[1] == board[4] == board[7]:
      return True
  if board[2] != "-":
    if board[2] == board[5] == board[8]:
      return True
  return False


def check_horizontal():
  if board[0] != "-":
    if board[0] == board[1] == board[2]:
      return True
  if board[3] != "-":
    if board[3] == board[4] == board[5]:
      return True
  if board[6] != "-":
    if board[6] == board[7] == board[8]:
      return True
  return False


def check_diagonal():
  if board[0] != "-":
    if board[0] == board[4] == board[8]:
      return True
  if board[2] != "-":
    if board[2] == board[4] == board[6]:
      return True
  return False


def player_turn(player):
  move = get_player_move(player)
  update_board_with_symbol_at_position(player, move)
  display_board()


def board_full():
  for element in board:
    if element == "-":
      return False
  else:
    return True


def play():
  global player
  print("Welcome to tic tac toe.")
  print("First player to play is " + player)
  display_board()

  while not check_win() and not board_full():
    player_turn(player)
    if check_win():
      print("\nCongrats player " + player + " !")
    switch_player()

  if board_full() and not check_win():
      print("Board is full. Game tie.")


def play_again():
  while True:
    return input("Play again?: ").lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh', 'oui']


def reset_board():
  global board
  board = [
            "-", "-", "-", 
            "-", "-", "-", 
            "-", "-", "-"]


play()
while play_again():
  reset_board()
  print("")
  play()
