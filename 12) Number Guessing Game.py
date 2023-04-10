#Number Guessing Game
import random
logo = '''
  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \        
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/                 _
                      | |              
 _ __  _   _ _ __ ___ | |__   ___ _ __ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| | | | |_| | | | | | | |_) |  __/ |   
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|
'''
print(logo)
print("Welcome to The Number Guessing Game!")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
num = random.choice(numbers)
print("I'm thinking of a number between 1 and 100")
print(f"pssst, the number is {num}")
difficulty = input("""Choose a difficulty level
1. Easy (type 'e')
2. Hard (type 'h')\n""")

if difficulty == 'e':
  life = 10
else:
  life = 5
  
guess = int(input("Make a guess: "))

while guess!=num:
  if guess!=num:
    life -= 1
    print(f"Wrong! You have {life} lives remaining")
    if guess > num:
      print("Guess a lower value")
    elif guess < num:
      print("Guess a higher value")
    if life == 0:
      print("Game Over.")
      break    
    guess2 = int(input("Make another guess: "))
    guess = guess2
    
if guess == num:
  print(f"You Won. The number was {num}")
