# #100days of code - day 9 - Blind Auction
from cleaner import clean

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
print("Welcome to the secret auction program.")

auction_bids = {}
to_continue = True

while to_continue:
    name = input("What is  your name?: ")
    bid = int(input("What's your bid?: $"))

    auction_bids[name] = bid

    cont = input("Are there any other bidder? Type 'yes' or 'no'. ")
    if cont == "no":
        to_continue = False
    clean()

highest_price = 0
winner_name = ""
for bidder in auction_bids:
    if auction_bids[bidder] > highest_price:
        highest_price = auction_bids[bidder]
        winner_name = bidder
    # print(highest_price, winner_name)

print(f"The winner is {winner_name} with a bid of ${highest_price}")
