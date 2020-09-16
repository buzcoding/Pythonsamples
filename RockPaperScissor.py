
import random from randint

#create a list with user options
lst = [Rock, Paper, Scissor]

#System user choice
computer=t[randint(0,2)]

#player option
player=False

while player == False:
  player=input('Rock, Paper, Scissor?')
  
  if player == computer:
    print("Tie!")
  elif player == 'Rock':
      if computer == 'paper':
        print("You lose", computer, "covers", player)
      else:
        print("You Win", computer, "smashes", player)
  elif player == 'Paper':
      if computer == 'Scissor':
        print("You lose", computer, "cut", player)
      else:
        print("You Win", computer, "covers", player)
  elif player == 'Scissor':
      if computer == 'Rock':
        print("You lose", computer, "smashes", player)
      else:
        print("You Win", computer, "cut", player)
   else:
      print("You entered wrong word")
   player == Flase
   computer = t[randint(0,2)]
  

