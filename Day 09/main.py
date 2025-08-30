bids = {}

MORE_BIDDERS = True

def find_highest_bidder(bids):
    winner = ''
    highest_bid = 0

    for bidder, bid_amount in bids.items():
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount

    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")


while MORE_BIDDERS:
    name = input("What is your name?\n").lower()
    bid = float(input("How much would you like to bid? $"))

    bids[name] = bid
    more_bids = input("Are there more bidders? 'yes' or 'no'.\n").lower()

    if more_bids == 'no':
        find_highest_bidder(bids)
        MORE_BIDDERS = False
