import random
user = input('''
Enter 'r' for rock
Enter 'p' for paper
Enter 's' for scissors\n
''')
#cpu_rock = 1
#cpu_paper = 2
#cpu_scissors = 3
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#CPU WITH ROCK
cpu = random.randint(1,3)
if cpu == 1 and user == 'r':
    print("Tie")
    print(f"User chose {rock}")
    print(f"CPU chose {rock}")
elif cpu == 1 and user == 'p':
    print("User wins")
    print(f"User chose {paper}")
    print(f"CPU chose {rock}")
elif cpu == 1 and user == 's':
    print("CPU wins")
    print(f"User chose {scissors}")
    print(f"CPU chose {rock}")

#CPU WITH PAPER
if cpu == 2 and user == 'r':
    print("CPU wins")
    print(f"User chose {rock}")
    print(f"CPU chose {paper}")
elif cpu == 2 and user == 'p':
    print("Tie")
    print(f"User chose {paper}")
    print(f"CPU chose {paper}")
elif cpu == 2 and user == 's':
    print("User wins")
    print(f"User chose {scissors}")
    print(f"CPU chose {paper}")

#CPU WITH SCISSORS
if cpu == 3 and user == 'r':
    print("User wins")
    print(f"User chose {rock}")
    print(f"CPU chose {scissors}")
elif cpu == 3 and user == 'p':
    print("CPU wins")
    print(f"User chose {paper}")
    print(f"CPU chose {scissors}")
elif cpu == 3 and user == 's':
    print("Tie")
    print(f"User chose {scissors}")
    print(f"CPU chose {scissors}")
