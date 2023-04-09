from replit import clear
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1,n2):
  return n1+n2
  
def subtract(n1,n2):
  return n1-n2
  
def divide(n1,n2):
  return n1/n2
  
def multiply(n1,n2):
  return n1*n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}
def calculator():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  
  for keys in operations:
    print(keys)
    
  operator = input("Enter operator: ")
  calculation_function = operations[operator]
  answer = calculation_function(num1,num2)
  print(f"{num1} {operator} {num2} = {answer}")
  
  decision = True
  while decision:
    ch = input(f"Type 'y' to continue calculating with {answer}, 'c' to start a new calculation or type 'n' to exit: ")
    if ch=='y':
      num3 = int(input("Next number:"))
      operator2 = input("Enter operator:")
      calculation_function2 = operations[operator2]
      answer2 = calculation_function2(answer,num3)
      print(f"{answer} {operator2} {num3} = {answer2}")
      answer = answer2
    elif ch=='c':
      clear()
      calculator()
    else:
      decision = False

calculator()
