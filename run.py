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
  "A1": ".", "A2": ".", "A3": ".", "A4": ".", "A5": ".",
  "B1": ".", "B2": ".", "B3": ".", "B4": ".", "B5": ".",
  "C1": ".", "C2": ".", "C3": ".", "C4": ".", "C5": ".",
  "D1": ".", "D2": ".", "D3": ".", "D4": ".", "D5": ".",
  "E1": ".", "E2": ".", "E3": ".", "E4": ".", "E5": ".",
  }

  board_computer = copy.copy(board_player)

  place_ships(board_player, board_computer)
  print_boards(name_player, board_player, board_computer)

  return name_player, board_player, board_computer


def place_ships(board1, board2):
  """
  Places 4 random ships with an @ on both game boards.
  """

  list_fields = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]

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

  print(board1["A1"], board1["A2"], board1["A3"], board1["A4"], board1["A5"])
  print(board1["B1"], board1["B2"], board1["B3"], board1["B4"], board1["B5"])
  print(board1["C1"], board1["C2"], board1["C3"], board1["C4"], board1["C5"])
  print(board1["D1"], board1["D2"], board1["D3"], board1["D4"], board1["D5"])
  print(board1["E1"], board1["E2"], board1["E3"], board1["E4"], board1["E5"])

  for k, v in board2.items():
    if v == "@":
      board2[k] = "."

  print("Computer")

  print(board2["A1"], board2["A2"], board2["A3"], board2["A4"], board2["A5"])
  print(board2["B1"], board2["B2"], board2["B3"], board2["B4"], board2["B5"])
  print(board2["C1"], board2["C2"], board2["C3"], board2["C4"], board2["C5"])
  print(board2["D1"], board2["D2"], board2["D3"], board2["D4"], board2["D5"])
  print(board2["E1"], board2["E2"], board2["E3"], board2["E4"], board2["E5"])


def main():
  name_player, board_player, board_computer = new_game()


main()
# Write your code to expect a terminal of 80 characters wide and 24 rows high


