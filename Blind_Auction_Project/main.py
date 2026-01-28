# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
bidders={}
def ask_bid():
    name = input("What is your name?:")
    bidders[name] = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == "yes":
        print("\n" * 100)
        ask_bid()
    else:
        highest = 0
        for name in bidders:
            if bidders[name] > highest:
                highest = bidders[name]
                winner = name
        print(f"The winner is {winner} with a bid of ${highest}")

ask_bid()





