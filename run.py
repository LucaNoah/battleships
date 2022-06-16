import random
import copy

class Board:
  """
  Main board class. Sets the game board which user and computer use.
  Has methods to place the ships, print the boards and shoot for user and computer.
  """
  def __init__(self, name):
    self.name = name
    self.board = {
            "f0": "*", "fA": "A", "fB": "B", "fC": "C", "fD": "D", "fE": "E",
            "f1": "1", "A1": ".", "B1": ".", "C1": ".", "D1": ".", "E1": ".",
            "f2": "2", "A2": ".", "B2": ".", "C2": ".", "D2": ".", "E2": ".",
            "f3": "3", "A3": ".", "B3": ".", "C3": ".", "D3": ".", "E3": ".",
            "f4": "4", "A4": ".", "B4": ".", "C4": ".", "D4": ".", "E4": ".",
            "f5": "5", "A5": ".", "B5": ".", "C5": ".", "D5": ".", "E5": ".",}

    self.place_ships()

  def place_ships(self):
    """
    Places 4 random ships with an @ on the board.
    """
    list_fields = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", 
            "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", 
            "E1", "E2", "E3", "E4", "E5"]
    position_ships = random.sample(list_fields, 4)

    for ship in position_ships:
      self.board[ship] = "@"

  def print_board(self, hide_ships = False):
    """
    Displays the boards with the option to hide or show the ships.
    """
    board_copy = copy.copy(self.board)

    for k, v in self.board.items():
      if hide_ships and v == "@":
        board_copy[k] = "."

    print(self.name)

    if hide_ships:
      print(" ".join(list(board_copy.values())[:6]))
      print(" ".join(list(board_copy.values())[6:12]))
      print(" ".join(list(board_copy.values())[12:18]))
      print(" ".join(list(board_copy.values())[18:24]))
      print(" ".join(list(board_copy.values())[24:30]))
      print(" ".join(list(board_copy.values())[30:36]))
    else:
      print(" ".join(list(self.board.values())[:6]))
      print(" ".join(list(self.board.values())[6:12]))
      print(" ".join(list(self.board.values())[12:18]))
      print(" ".join(list(self.board.values())[18:24]))
      print(" ".join(list(self.board.values())[24:30]))
      print(" ".join(list(self.board.values())[30:36]))

  def shoot_user(self, name):
    """
    Ask the player for a position to shoot at. 
    If there is an enemy ship at this position, it will be marked with an 'x'. 
    If there is no enemy ship there, this position is marked with a '/'. 
    If the position has already been shot at, the player is asked to enter a new position.
    """
    list_banned_input = [
      "f0", "f1", "f2", "f3", "f4", "f5", 
      "fA", "fB", "fC", "fD", "fE"]

    while True:
      try:
        target_player = input("Guess a target:\n")

        if target_player in list_banned_input:
          print(f"{target_player} is not a valid position!")
        elif self.board[target_player] == ".":
          self.board[target_player] = "/"
          print(f"{name} you missed!")
          break
        elif self.board[target_player] == "@":
          self.board[target_player] = "x"
          print(f"{name} you have destroyed an enemy ship!")
          break
        elif self.board[target_player] == "/" or "x":
          print("This position has already been fired at, choose another!")

      except KeyError:
        print(f"{target_player} is not a valid position!")


  def shoot_computer(self):
    """
    Create a random position for the computer to fire at.
    If there is an enemy ship at this position, it will be marked with an 'x'. 
    If there is no enemy ship there, this position is marked with a '/'.
    The computer can not shoot the same position twice.
    """
    list_fields = [
    "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5",
    "E1", "E2", "E3", "E4", "E5"]
      
    while True:
      target_computer = random.sample(list_fields, 1)

      if self.board[target_computer[0]] == ".":
        self.board[target_computer[0]] = "/"
        print("Computer missed!")
        break
      elif self.board[target_computer[0]] == "@":
        self.board[target_computer[0]] = "x"
        print("Computer has destroyed one of your ships")
        break

def play_game(name, board1, board2):
  """
  Lets both parties shoot/game until one of them wins.
  """
  while True:
    board2.shoot_user(name)
    board1.shoot_computer()
    board1.print_board()
    board2.print_board(hide_ships = False)

    if not "@" in board2.board.values():
      print(f"Game Over! {name} you win!")
      return False
    elif not "@" in board1.board.values():
      print("Game Over! Computer win!")
      return False

def game_info():
  """
  Prints a welcome message and game rules.
  """
  print("Welcome to Battleships!")
  print("Rules:\n4 ships are randomly distributed on 2 boards and marked with an '@'.\nNow the player has to guess a field on the opponent's board.\nHits are marked with an 'x', misses with a '/'.\nAfter the player has guessed, the computer chooses a random field.\nThis continues until one of the two parties destroys all enemy ships.")

def get_user_name():
  """
  Get the user name and check if the entered name contains at least 1 letter.
  """
  while True:
    name = input("Enter you name:\n")

    if len(name) == 0:
      print("Please enter a name with at least one letter!")
    else:
      return name

def main():
  """
  Starts the game.
  """
  game_info()
  user_name = get_user_name()
  print(f"Ahoy Captain {user_name}!")
  print("May there always be a guiding light on all of your journeys \n& water under the keel.")
  user_board = Board(user_name)
  computer_board = Board("Computer")
  user_board.print_board()
  computer_board.print_board(hide_ships = False)
  print("Please enter your targets in the following format: 'A1' or 'E5'")
  play_game(user_name, user_board, computer_board)
  raise SystemExit

main()