from replit import clear
import art

print(art.logo)
should_repat = True

while should_repat:
  name = input("What is your name? ")
  bid = int (input("What is your bid?$"))
  bid_dict = {}
  bid_dict[name] = bid
  new_bid =input("Are there any other bidders? Type 'yes' or 'no'")
  if new_bid == "yes":
    clear()
  elif new_bid == "no":
    should_repat=False
    max_bid = max(bid_dict.values())
    print(f"The maximum bid is {max_bid}$ of {name}")
