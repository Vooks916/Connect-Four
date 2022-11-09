#Define the global variables
player_turn = 'X'
game_over = False
board = [
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

#Resets the board at end of game
def clear_board(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      board[row][col] = ' '

#Prints the board to the console
def display_board(board):
  top_line = '  1   2   3   4   5   6   7  '
  horizontal_divider = '+---+---+---+---+---+---+---+'
  blank_space = '\n' * 6

  print(blank_space)
  print(top_line)
  for i in range(len(board)):
    current_line = ''
    
    for j in range(len(board[i])):
      current_line += '| '
      current_line += board[i][j] + ' '
    
    current_line += '|'
    print(horizontal_divider)
    print(current_line)

  print(horizontal_divider)
  print()

#Checks if selected column is valid, then places piece as far down as possible, displays the current board, and changes player_turn
def select_space(player, col):
  global player_turn
  valid_columns = [i for i in range(1, len(board[0]) + 1)]
  valid_players = ['X', 'O']
  if col not in valid_columns:
    display_board(board)
    print('It is %s\'s turn.' % (player))
    print('\nMake sure to pick a valid column between 1 and 7.')
    return False

  if player not in valid_players:
    display_board(board)
    print('It is %s\'s turn.' % (player))
    print('\nMake sure to only use an \'X\' or an \'O\'.')
    return False

  if board[0][col - 1] != ' ':
    display_board(board)
    print('It is %s\'s turn.' % (player))
    print('\nMake sure to pick a column that is not full.')
    return False

  col_height = len(board)
  for i in range(0, col_height):
    if board[col_height - (i + 1)][col - 1] == ' ':
      board[col_height - (i + 1)][col - 1] = player
      break
  
  display_board(board)
  print('Placed an %s in column %s \n' % (player, str(col)))
  if player_turn == 'X':
    player_turn = 'O'
  else:
    player_turn = 'X'
  return True

#Checks for 4 in a row vertically
def check_vertical_win(player, last_row, last_col):
  num_in_col = 0
  for i in range(4):
    if last_row + i > 5:
      break
    if board[last_row + i][last_col] == player:
      num_in_col += 1
    else:
      break
    
    if num_in_col == 4:
      return True

#Checks for 4 in a row horizontally
def check_horizontal_win(player, last_row, last_col):
  num_in_row = 0
  for i in range(4):
    if last_col - i < 0 or board[last_row][last_col - i] != player:
      break
    if board[last_row][last_col - i] == player:
      num_in_row += 1
    else:
      break

  for i in range(1, 4):
    if last_col + i > 6:
      break
    if board[last_row][last_col + i] == player:
      num_in_row += 1
    else:
      break
    
  if num_in_row >= 4:
    return True

#checks for 4 in a row along / diagnal
def check_right_diag_win(player, last_row, last_col):
  num_in_right_diag = 0
  for i in range(4):
    if last_row + i > 5 or last_col - i < 0 or board[last_row + i][last_col - i] != player:
      break
    if board[last_row + i][last_col - i] == player:
      num_in_right_diag += 1
    else:
      break

  for i in range(1, 4):
    if last_row - i < 0 or last_col + i > 6 or board[last_row - i][last_col + i] != player:
      break
    if board[last_row - i][last_col + i] == player:
      num_in_right_diag += 1
    else:
      break

  if num_in_right_diag >= 4:
    return True

#checks for 4 in a row along \ diagnal
def check_left_diag_win(player, last_row, last_col):
  num_in_left_diag = 0
  for i in range(4):
    if last_row + i > 5 or last_col + i > 6 or board[last_row + i][last_col + i] != player:
      break
    if board[last_row + i][last_col + i] == player:
      num_in_left_diag += 1
    else:
      break

  for i in range(1, 4):
    if last_row - i < 0 or last_col - i < 0 or board[last_row - i][last_col - i] != player:
      break
    if board[last_row - i][last_col - i] == player:
      num_in_left_diag += 1
    else:
      break

  if num_in_left_diag >= 4:
    return True

#combines all 4 possible wins to one function, returns true if any single check is also true
def check_for_win(player, last_row, last_col):
  ver = check_vertical_win(player, last_row, last_col)
  hor = check_horizontal_win(player, last_row, last_col)
  lef = check_right_diag_win(player, last_row, last_col)
  rig = check_left_diag_win(player, last_row, last_col)

  if ver or hor or lef or rig:
    return True
  else:
    return False

#Checks if entire top row is true, returns true
def check_for_tie():
  top_spaces_used = 0
  for i in range(len(board[0])):
    if board[0][i] != ' ':
      top_spaces_used += 1
  if top_spaces_used == len(board[0]):
    return True
  else:
    return False

#Calculates the last row a piece was placed in
def find_last_row(col):
  last_row = 0
  for i in range(len(board)):
    if board[i][col - 1] == ' ':
      last_row += 1
  return last_row

#Displays board and player_turn. Asks for column input, then checks for a win/tie
def turn(player):
  global game_over
  valid_selection = False
  display_board(board)
  print('It is %s\'s turn.' % (player))
  while valid_selection == False:
    column = input("Please choose a column between 1 and 7. \n")
    if column.isdigit():
      column = int(column)
      valid_selection = select_space(player, column)
      if valid_selection == True:
        row = find_last_row(column)
        won = check_for_win(player, row, column - 1)
        tie = check_for_tie()

        if won == True:
          game_over = True
          print('Congratulations! %s won the game!' % (player))

        if tie == True and won == False:
          game_over = True
          print('Good game! You tied!')

    else: 
      display_board(board)
      print('It is %s\'s turn.' % (player))
      print('\nPlease enter a whole number.')
  
#Runs turn() while the game is ongoing, then runs play_again()
def play_game():
  while game_over == False:
    turn(player_turn)
  play_again()

#asks if player wants to play another game
def play_again():
  global game_over
  global board
  while True:
    play_again = input('Do you want to play again? (Y/N) \n')
    if play_again.lower() == 'y':
      game_over = False
      clear_board(board)
      play_game()
      break
    elif play_again.lower() == 'n':
      break
    else:
      print('Please enter either \'Y\' (yes) or \'N\' (no).')

play_game()