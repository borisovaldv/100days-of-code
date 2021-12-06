from art import logo
from replit import clear

print(logo)

bids = {}
finish = False


def highest_bidder(bids):
    highest_price = 0
    name_of_bidder = ''
    for v, k in bids.items():
        if k > highest_price:
            name_of_bidder = v
            highest_price = k
    print(f"The winner is {name_of_bidder} with a bid of ${highest_price}")


while not finish:
    name = input('What is your name?\n')
    price = int(input('What is your bid?\n$'))
    bids[name] = price

    other_bidders = input('Are there any other bidders? Type "yes" or "no"\n')

    if other_bidders == 'no':
        finish = True
        highest_bidder(bids)
    if other_bidders == 'yes':
        clear()
