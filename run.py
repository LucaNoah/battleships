import random
import copy

def new_game():
  """
  Prints a welcome message, asks user for name and prints the rules and game info.
  Creates 2 game boards one for player one for computer. 
  ??? SANDEEP places the ships and displays the game boards. ???
  """

  print("Welcome to Battleships!")

  name_player = input("Enter your name: ")

  print("RULES, blbalablalbalbalablablabalballbalbalba")

  board_player = {
  "f0": "*", "fA": "A", "fB": "B", "fC": "C", "fD": "D", "fE": "E",
  "f1": "1", "A1": ".", "B1": ".", "C1": ".", "D1": ".", "E1": ".",
  "f2": "2", "A2": ".", "B2": ".", "C2": ".", "D2": ".", "E2": ".",
  "f3": "3", "A3": ".", "B3": ".", "C3": ".", "D3": ".", "E3": ".",
  "f4": "4", "A4": ".", "B4": ".", "C4": ".", "D4": ".", "E4": ".",
  "f5": "5", "A5": ".", "B5": ".", "C5": ".", "D5": ".", "E5": ".",
  }

  board_computer = copy.copy(board_player)

  place_ships(board_player, board_computer)
  print_boards(name_player, board_player, board_computer)

  return name_player, board_player, board_computer


def place_ships(board1, board2):
  """
  Places 4 random ships with an @ on both game boards.
  """

  list_fields = [
    "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", 
    "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", 
    "E1", "E2", "E3", "E4", "E5"]

  ships_player = random.sample(list_fields, 4)

  ships_computer = random.sample(list_fields, 4)

  board1[ships_player[0]] = "@"
  board1[ships_player[1]] = "@"
  board1[ships_player[2]] = "@"
  board1[ships_player[3]] = "@"

  board2[ships_computer[0]] = "@"
  board2[ships_computer[1]] = "@"
  board2[ships_computer[2]] = "@"
  board2[ships_computer[3]] = "@"


def print_boards(name, board1, board2):
  """
  Displays the two game boards, the one of the computer does not show the ships.
  """

  print(name)

  print(board1["f0"], board1["fA"], board1["fB"], board1["fC"], board1["fD"], board1["fE"])
  print(board1["f1"], board1["A1"], board1["B1"], board1["C1"], board1["D1"], board1["E1"])
  print(board1["f2"], board1["A2"], board1["B2"], board1["C2"], board1["D2"], board1["E2"])
  print(board1["f3"], board1["A3"], board1["B3"], board1["C3"], board1["D3"], board1["E3"])
  print(board1["f4"], board1["A4"], board1["B4"], board1["C4"], board1["D4"], board1["E4"])
  print(board1["f5"], board1["A5"], board1["B5"], board1["C5"], board1["D5"], board1["E5"])

  board2_noships = copy.copy(board2)

  for k, v in board2_noships.items():
    if v == "@":
      board2_noships[k] = "."

  print("Computer")

  print(board2_noships["f0"], board2_noships["fA"], board2_noships["fB"], board2_noships["fC"], board2_noships["fD"], board2_noships["fE"])
  print(board2_noships["f1"], board2_noships["A1"], board2_noships["B1"], board2_noships["C1"], board2_noships["D1"], board2_noships["E1"])
  print(board2_noships["f2"], board2_noships["A2"], board2_noships["B2"], board2_noships["C2"], board2_noships["D2"], board2_noships["E2"])
  print(board2_noships["f3"], board2_noships["A3"], board2_noships["B3"], board2_noships["C3"], board2_noships["D3"], board2_noships["E3"])
  print(board2_noships["f4"], board2_noships["A4"], board2_noships["B4"], board2_noships["C4"], board2_noships["D4"], board2_noships["E4"])
  print(board2_noships["f5"], board2_noships["A5"], board2_noships["B5"], board2_noships["C5"], board2_noships["D5"], board2_noships["E5"])

  #if you want to see computer ships printed uncomment code below

  print(board2["f0"], board2["fA"], board2["fB"], board2["fC"], board2["fD"], board2["fE"])
  print(board2["f1"], board2["A1"], board2["B1"], board2["C1"], board2["D1"], board2["E1"])
  print(board2["f2"], board2["A2"], board2["B2"], board2["C2"], board2["D2"], board2["E2"])
  print(board2["f3"], board2["A3"], board2["B3"], board2["C3"], board2["D3"], board2["E3"])
  print(board2["f4"], board2["A4"], board2["B4"], board2["C4"], board2["D4"], board2["E4"])
  print(board2["f5"], board2["A5"], board2["B5"], board2["C5"], board2["D5"], board2["E5"])


def shoot_player(name, board2):
  """
  Ask the player for a position to shoot at. 
  If there is an enemy ship at this position, it will be marked with an 'x'. 
  If there is no enemy ship there, this position is marked with a '/'. 
  If the position has already been shot at, the player is asked to enter a new position.
  """

  list_banned_input = [
  "f0", "f1", "f2", "f3", "f4", "f5", 
  "fA", "fB", "fC", "fD", "fE"
  ]

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
  "E1", "E2", "E3", "E4", "E5"
  ]

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

