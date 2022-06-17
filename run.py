import random
import copy


WELCOME_MESSAGE = """
Welcome to Battleships!
Rules:
* 4 ships are randomly distributed on 2 boards and marked with an '@'.
* Now the player has to guess a field on the opponent's board.
* Hits are marked with an 'x', misses with a '/'.
* After the player has guessed, the computer chooses a random field.
* This continues until one of the two parties destroys all enemy ships.
"""

GAME_START_MESSAGE_TEMPLATE = """
Ahoy Captain {user_name}!
May there always be a guiding light on all of your journeys 
& water under the keel.
"""


class Board:
  """
  Main board class. Sets the game board which user and computer use.
  Has methods to place the ships, print the boards and shoot for user 
  and computer.
  """

  INITIAL_GAME_BOARD = {
            "f0": "*", "fA": "A", "fB": "B", "fC": "C", "fD": "D", "fE": "E",
            "f1": "1", "A1": ".", "B1": ".", "C1": ".", "D1": ".", "E1": ".",
            "f2": "2", "A2": ".", "B2": ".", "C2": ".", "D2": ".", "E2": ".",
            "f3": "3", "A3": ".", "B3": ".", "C3": ".", "D3": ".", "E3": ".",
            "f4": "4", "A4": ".", "B4": ".", "C4": ".", "D4": ".", "E4": ".",
            "f5": "5", "A5": ".", "B5": ".", "C5": ".", "D5": ".", "E5": "."}

  VALID_POSITIONS = [
        "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", 
        "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", 
        "E1", "E2", "E3", "E4", "E5"]

  INVALID_POSITIONS = [
      "f0", "f1", "f2", "f3", "f4", "f5", 
      "fA", "fB", "fC", "fD", "fE"]


  def __init__(self, name):
    self.name = name
    self.board = copy.copy(self.INITIAL_GAME_BOARD)

    self.place_ships()

  def place_ships(self):
    """
    Places 4 random ships with an @ on the board.
    """
    
    position_ships = random.sample(self.VALID_POSITIONS, 4)

    for ship in position_ships:
      self.board[ship] = "@"

  def print_board(self, hide_ships=False):
    """
    Displays the boards with the option to hide or show the ships.

    Args:
    hide_ships: Whether to show the actual ship position.
    This is useful when you want to see the computers ships.
    """
    board_copy = copy.copy(self.board)

    for k, v in self.board.items():
      if hide_ships and v == "@":
        board_copy[k] = "."

    print(self.name)

    board_to_print = board_copy if hide_ships else self.board

    print(" ".join(list(board_to_print.values())[:6]))
    print(" ".join(list(board_to_print.values())[6:12]))
    print(" ".join(list(board_to_print.values())[12:18]))
    print(" ".join(list(board_to_print.values())[18:24]))
    print(" ".join(list(board_to_print.values())[24:30]))
    print(" ".join(list(board_to_print.values())[30:36]))

  def shoot_user(self):
    """
    Ask the player for a position to shoot at. 
    If there is an enemy ship at this position, it will be marked with an 'x'. 
    If there is no enemy ship there, this position is marked with a '/'. 
    If the position has already been shot at, the player is asked to enter a 
    new position.
    """

    while True:
      try:
        target_player = input("Guess a target:\n").upper()

        if target_player in self.INVALID_POSITIONS:
          print(f"{target_player} is not a valid position!")
        elif self.board[target_player] == ".":
          self.board[target_player] = "/"
          print(f"{self.name} you missed!")
          break
        elif self.board[target_player] == "@":
          self.board[target_player] = "x"
          print(f"{self.name} you have destroyed an enemy ship!")
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
      
    while True:
      target_computer = random.sample(self.VALID_POSITIONS, 1)

      if self.board[target_computer[0]] == ".":
        self.board[target_computer[0]] = "/"
        print("Computer missed!")
        break
      elif self.board[target_computer[0]] == "@":
        self.board[target_computer[0]] = "x"
        print("Computer has destroyed one of your ships")
        break

  def all_ships_destroyed(self):
    """
    Checks if there is a ship left on the board.
    """
    return "@" not in self.board.values()


def play_game(user_board, computer_board):
  """
  Lets both parties shoot/game until one of them wins.
  """
  while True:
    computer_board.shoot_user()
    user_board.shoot_computer()

    user_board.print_board()
    computer_board.print_board(hide_ships=True)

    if computer_board.all_ships_destroyed():
      print(f"Game Over! {user_board.name} you win!")
      break

    if user_board.all_ships_destroyed():
      print("Game Over! Computer win!")
      break



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
  print(WELCOME_MESSAGE)
  user_name = get_user_name()
  print(GAME_START_MESSAGE_TEMPLATE.format(user_name=user_name))

  user_board = Board(user_name)
  computer_board = Board("Computer")

  user_board.print_board()
  computer_board.print_board(hide_ships=False)

  print("Please enter your targets in the following format: 'A1' or 'e5'")
  play_game(user_board, computer_board)
  
  exit(0)

if __name__ == "__main__":
  main()
