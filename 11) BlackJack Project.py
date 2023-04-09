from replit import clear
import random
############### Blackjack Project #####################
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play_game = input("Do you want to play a game of BlackJack? 'y or 'n':")
if play_game == 'y':
  clear()
  print(""" _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                                                              
       ,'`.    _  _    /\    _(_)_
      (_,._)  ( `' )  <  >  (_)+(_)
        /\     `.,'    \/      |
        
        """)

u1 = random.choice(cards)
u2 = random.choice(cards)
user_cards = [u1,u2]
current_score = u1+u2
print(f"Your cards: {user_cards}, current score: {current_score}")

c1 = random.choice(cards)
c2 = random.choice(cards)
computer_cards = [c1,c2]
computer_score = c1+c2
print(f"Computer's first card: {c1}")

game_continue = True
while game_continue:
  ch = input("Type 'y' to get another card, 'n' to pass: ")
  if ch=='y':
    u3 = random.choice(cards)
    print(f"your new card: {u3}")
    user_cards.append(u3)
    current_score += u3
    print("---------------")
    print(f"Your final hand: {user_cards}, final score: {current_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  if ch=='n':
    print("---------------")
    print(f"Your final hand: {user_cards}, final score: {current_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  if current_score>21 and computer_score<=21:
    print("You went over. You Lose")
  elif computer_score>21 and current_score<=21:
    print("Computer went over. You Win")
  elif current_score<=21 and computer_score<current_score:
    print("You Win")
  elif computer_score<=21 and current_score<computer_score:
    print("Computer Wins")
  elif computer_score == current_score:
    print("Draw")
    
  play_again = input("Do you want to play again? 'y' or 'n': ")
  if play_again == 'y':
    clear()
    u1 = random.choice(cards)
    u2 = random.choice(cards)
    user_cards = [u1,u2]
    current_score = u1+u2
    print(f"Your cards: {user_cards}, current score: {current_score}")
    c1 = random.choice(cards)
    c2 = random.choice(cards)
    computer_cards = [c1,c2]
    computer_score = c1+c2
    print(f"Computer's first card: {c1}")
    game_continue = True
  else:
    print("GoodBye")
    game_continue = False
