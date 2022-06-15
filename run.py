import random
import copy

class Board:
  """
  """
  def __init__(self, name):
    """
    """
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

  def print_boards(self, hide_ships = False):
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

def shoot_player(name, board2):
  """
  Ask the player for a position to shoot at. 
  If there is an enemy ship at this position, it will be marked with an 'x'. 
  If there is no enemy ship there, this position is marked with a '/'. 
  If the position has already been shot at, the player is asked to enter a new position.
  """
  list_banned_input = [
  "f0", "f1", "f2", "f3", "f4", "f5", 
  "fA", "fB", "fC", "fD", "fE"]
  shoot = True

  while shoot == True:
    try:
      target_player = input("Guess a target: ")

      if target_player in list_banned_input:
        print(f"{target_player} is not a valid position!")
      elif board2[target_player] == ".":
        board2[target_player] = "/"
        print(f"{name} you missed!")
        shoot = False
      elif board2[target_player] == "@":
        board2[target_player] = "x"
        print(f"{name} you have destroyed an enemy ship!")
        shoot = False
      elif board2[target_player] == "/" or "x":
        print("This position has already been fired at, choose another!")

    except KeyError:
      print(f"{target_player} is not a valid position!")


def shoot_computer(board1):
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
  shoot = True

  while shoot == True:
    target_computer = random.sample(list_fields, 1)

    if board1[target_computer[0]] == ".":
      board1[target_computer[0]] = "/"
      print("Computer missed!")
      shoot = False
    elif board1[target_computer[0]] == "@":
      board1[target_computer[0]] = "x"
      print("Computer has destroyed one of your ships")
      shoot = False
    elif board1[target_computer[0]] == "/" or "x":
      shoot = True

def main():
  """
  Starts the game. Lets both parties shoot/game until one of them wins.
  """
  name_player, board_player, board_computer = new_game()

  while True:
    shoot_player(name_player, board_computer)

    shoot_computer(board_player)

    print_boards(name_player, board_player, board_computer)

    if not "@" in board_computer.values():
      print(f"Game Over! {name_player} you win!")
      return False
    elif not "@" in board_player.values():
      return False
      print("Game Over! Computer win!")


main()
# Write your code to expect a terminal of 80 characters wide and 24 rows high


