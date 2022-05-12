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

  
# Write your code to expect a terminal of 80 characters wide and 24 rows high
