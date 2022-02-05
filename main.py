from random import randint
from art import logo

EASY_LEVEL_TURNS= 10
HARD_LEVEL_TURNS= 5




def check_answer(guess,answer,turns) :
  """Checks answer against guess, Returns the number of turns remaining."""
  
  if guess>answer :
   print("Too High")
   return turns -1
  elif guess<answer :
    print("Too Low")
    return turns -1
  else :
    print(f"You got it Right !! The Answer is {answer}")  

  


def set_difficulty() :
  level= input("Choose a difficulty 'Easy' or 'Hard' : ").lower()  
  if level== "easy" :
    return EASY_LEVEL_TURNS
  else :
    return HARD_LEVEL_TURNS  


def game() :
  print(logo)
  print("Welcome to Number Guessing Game !!")
  print("I'm thinking of a number between 1 to 100 !!")
  answer= randint(1,100)
 

  turns= set_difficulty()
 


  guess= 0
  while guess != answer :
    print(f"You have {turns} attenpts remaining to Guess the Number")

    guess= int(input("Make a Guess : "))

    turns= check_answer(guess,answer,turns)
    if turns== 0 :
      print("You Ran out of Turns, you Loose !!")
      return 
    elif guess != answer :
      print("Guess Again") 



game()
