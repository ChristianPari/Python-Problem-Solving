# Mastermind Game
"""
A CLI game that allows the user to play aganist the computer! The computer randomly generates a 4 digit code w/ digits between 0 and 9, and the user has to try and guess the code.

If there is a correct number in the correct spot then there will be a "black peg" in the response, if there is a correct number in the wrong spot then there will be a "white peg".

Can you win?!
"""

# function to generate a random number
def gen_random_num():
  # generate random integer values
  from random import randint

  value = []

  # generate some integers
  for _ in range(4):
    value.append("{}".format(randint(0, 5)))

  code = "".join(value)

  return code

# function to begin program
def start():
  # winning code genereated
  win_code = gen_random_num()
  # code passed to the questions to check later aganist user input
  question1(win_code)

# first question, takes and passes the winning code to following functions
def question1(code):
  print("\nWelcome to Mastermind!\nPlease enter your guess, 4 numbers between 0 and 9, ex: 1234")
  user_guess = guessing(input("Guess: "), code, [])

# function to compare the user's input aganist the winning code
def guessing(guess, winning_code, guesses):
  def convert_to_list(string):
      numbers = []
      numbers[:0] = string
      return numbers


  winning_code_list = convert_to_list(winning_code)
  user_guess_list = convert_to_list(guess)

  response = {"black": 0, "white": 0}
  guess_list = guesses

  # creating a response based on what the user has guessed, how many are correct or in wrong places
  for idx, val in enumerate(winning_code_list):
    if (val == user_guess_list[idx]):
      response["black"] += 1
    elif (user_guess_list.__contains__(val) == True):
      response["white"] += 1

  # possible responses from program
  if (response["black"] == winning_code_list.__len__()):
    play_again = input("\nYou Win!! Play again?\nY/N: ").lower()
    if (play_again.startswith("y")):
      start()
    else:
      print("\nGood Game!")
  else:
    if (guess_list.__len__() == 9):
      play_again = input("\nGame Over. Play again?\nY/N: ").lower()
      if (play_again.startswith("y")):
        start()
      else:
        print("Better luck next time!")
    else: 
      guess_list.append(guess)

      print("\n{} correct an in the right spot, {} correct but in wrong spot".format(response["black"], response["white"]))

      guesses_string = ", ".join(guess_list)

      print("\nYour guesses: {}".format(guesses_string))
      
      if (guess_list.__len__() == 8):
        print("\nLast try!!")

      guessing(input("\nGuess: "), winning_code, guess_list)

# start the program
start()