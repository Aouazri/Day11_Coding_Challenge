import random
from replit import clear
from art import logo
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
#I'm trying this on Expert level difficulty, let's go x) 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


## ******************* deal function ******************* ##
def deal_card(list):
  random_card = random.choice(cards)
  return list.append(random_card)
## ******************* ************ ******************* ##
## ******************* calculate score function ******************* ##
def calculate_score(list):
  score= sum(list)
  if score==21 and len(list) == 2: 
    return 0
  #Handling the Ace case, if the score is above 21 we consider the Ace(11) as 1. 
  if 11 in list and score>21:
    list.remove(11)
    list.append(1)
    score= sum(list)
  return score
## ******************* ************ ******************* ##
def play():
  print(logo)
  random.shuffle(cards)
  user_cards = []
  computer_cards= []
  for i in range(2): 
    deal_card(user_cards)
  #user_score = sum(user_cards)
  user_score = calculate_score(user_cards)
  
  print(f"   Your cards: {user_cards}, current score: {user_score}")
  computer_first_card= random.choice(cards)
  computer_cards.append(computer_first_card)
  print(f"   Computer's first card: {computer_first_card}")

  
  ## ************************ ************************* ##
  if not(user_score == 0 ):
    another_card= input("Type 'y' to get another card; type 'n' to pass: ").lower()
  else: 
    another_card= 'n'
  while another_card =='y'and user_score<=21:
    deal_card(user_cards)
    user_score= calculate_score(user_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_first_card}")
    if user_score>21: 
      break
    another_card= input("Type 'y' to get another card; type 'n' to pass: ").lower()
    
    ## ************************ ************************* ##
    
  computer_score= calculate_score(computer_cards)
  ## while computer score under 17 we deal another card ##
  while computer_score<17: 
    deal_card(computer_cards)
    computer_score= calculate_score(computer_cards)
  ## ************************************************** ##
  print(f"   Your cards: {user_cards}, final score: {user_score}")
  print(f"   computer cards {computer_cards}, final score: {computer_score}")
  ## ************************************************** ##

  ## *********************** Check Results *********************** ##
  ## *******************  BLACKJACK ************* ## 
  def compare_score(computer_score, user_score):
    if computer_score == 0 :
      print("You lost, your opponent has a BLACKJACK!! \U0001F62D \n ")
    elif user_score == 0 :
      print("You WIN with a BLACKJACK!! \U0001F929 \n ")
      ## ************************************************** ##
    elif user_score>21:
      print("You went over, you lose! \U0001F622 \n ")
    elif computer_score>21:
      print("Opponent went over. You win! \U0001f600 \n ")
    elif user_score< computer_score and computer_score<=21: 
      print("You lose \U0001F622 \n ")
    elif user_score == computer_score:
      print("It's a draw \U0001F91D \n ")
    else: 
      print('You win! \U0001f600 \n ')
  compare_score(computer_score, user_score)
  ## *************************************************************** ##
  should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n ").lower()
  if should_continue =='y':
    clear()
    play()
  else:
    print("Thank you for playing, hope you had fun! \U0001F60E")
play_game= input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower()
if play_game =='y':
  clear()
  play()




