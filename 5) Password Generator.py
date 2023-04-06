#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

psswd = ""

for i in range(0,nr_letters):
  a = random.randint(0,len(letters)-1)
  psswd += letters[a]

for i in range(0,nr_symbols):
  a = random.randint(0,len(symbols)-1)
  psswd += symbols[a]

for i in range(0,nr_numbers):
  a = random.randint(0,len(numbers)-1)
  psswd += numbers[a]

print("Password : "+psswd)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

psswd_2 = []
newPass = ""

for i in range(0,nr_letters):
  a = random.randint(0,len(letters)-1)
  psswd_2 += letters[a]

for i in range(0,nr_symbols):
  a = random.randint(0,len(symbols)-1)
  psswd_2 += symbols[a]

for i in range(0,nr_numbers):
  a = random.randint(0,len(numbers)-1)
  psswd_2 += numbers[a]

for password in psswd_2:
  b = random.randint(0,len(psswd_2)-1)
  newPass  += psswd_2[b]

print("Password++ : "+newPass)
