import re
from random import randint

from alpha_beta import mini_max_ab

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    selected_cell = self.board
    #rows
    opt1 = (selected_cell[0] == selected_cell[1] == selected_cell[2] and selected_cell[0] is not None, selected_cell[0])
    opt2 = (selected_cell[3] == selected_cell[4] == selected_cell[5] and selected_cell[3] is not None, selected_cell[3])
    opt3 = (selected_cell[6] == selected_cell[7] == selected_cell[8] and selected_cell[6] is not None, selected_cell[6])
    #columns
    opt4 = (selected_cell[0] == selected_cell[3] == selected_cell[6] and selected_cell[0] is not None, selected_cell[0])
    opt5 = (selected_cell[1] == selected_cell[4] == selected_cell[7] and selected_cell[1] is not None, selected_cell[1])
    opt6 = (selected_cell[2] == selected_cell[5] == selected_cell[8] and selected_cell[2] is not None, selected_cell[2])
    #diagonals
    opt7 = (selected_cell[0] == selected_cell[4] == selected_cell[8] and selected_cell[0] is not None, selected_cell[0])
    opt8 = (selected_cell[2] == selected_cell[4] == selected_cell[6] and selected_cell[2] is not None, selected_cell[2])

    opt_list = [opt1, opt2, opt3, opt4, opt5, opt6, opt6, opt7, opt8]
    draw = False
    for i in range(0,9):

        if(opt_list[i][0]):
            if(opt_list[i][1] == _PLAYER_SYMBOL):
                self.winner= _PLAYER
                self.is_game_over = True
            else:
                self.winner = _MACHINE
                self.is_game_over = True
            return True

    if(self.board.count(None) == 0):
        self.winner = None
        self.is_game_over = True
        return True

    return False

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    #value = randint(0,8)
    #while(self.board[value] is not None):
     #   value = randint(0,8)
    #self.board[value] = _MACHINE_SYMBOL
    #print(mini_max_ab(self.board, False, _MACHINE_SYMBOL, -1, -1)[1])
    self.board = mini_max_ab(self.board, False, _MACHINE_SYMBOL, -9999, 9999)[1]



  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
     print("And winner is: {0}.".format(self.winner) if self.winner is not None else "Draw.")



  #------------------------------Poda-------------------------------------------
