# Dictionaries and Nesting

dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


# for key, value in dict.items():
#     print(key, value)
#     print(dict[key])

from logo import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: €"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "yes":
        # clear scre
        import os

        os.system("cls" if os.name == "nt" else "clear")

    elif should_continue == "no":
        bidding_finished = True
        highest_bid = 0
        winner = ""
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bid = bids[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of €{highest_bid}.")
