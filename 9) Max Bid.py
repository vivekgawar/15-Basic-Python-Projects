from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")
bidding_dict = {}

otherbids = True
total_bids = 0
while otherbids:
  name = input("What is your name?:")
  bid = int(input("What is your bid?: Rs."))
  other_bids = input("Are there any other bidders? Type 'yes' or 'no'.")
  clear()
  total_bids += 1
  for i in range(total_bids):
    bidding_dict[name] = bid 
  if other_bids=="no":
    otherbids = False

max_bid = max(bidding_dict.values())
max_bidder = max(bidding_dict, key = bidding_dict.get)
print(f"The winner is {max_bidder} with a bid of Rs.{max_bid}")
