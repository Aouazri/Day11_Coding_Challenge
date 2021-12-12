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
    card_choice= random.choice(cards)
    user_cards.append(card_choice)
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
    computer_score= sum(computer_cards)
  ## ************************************************** ##
  print(f"   Your cards: {user_cards}, final score: {user_score}")
  print(f"   computer cards {computer_cards}, final score: {computer_score}")
  ## ************************************************** ##

  ## *********************** Check Results *********************** ##
  ## *******************  BLACKJACK ************* ## 
  def compare_score(computer_score, user_score):
    if computer_score == 0 :
      print("You lost, your opponent has a BLACKJACK!! \U0001F62D")
    elif user_score == 0 :
      print("You WIN with a BLACKJACK!! \U0001F929")
      ## ************************************************** ##
    elif user_score>21:
      print("You went over, you lose! \U0001F622 ")
    elif computer_score>21:
      print("Opponent went over. You win! \U0001f600")
    elif user_score< computer_score and computer_score<=21: 
      print("You lose \U0001F622")
    elif user_score == computer_score:
      print("It's a draw \U0001F91D")
    else: 
      print('You win! \U0001f600')
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



##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

