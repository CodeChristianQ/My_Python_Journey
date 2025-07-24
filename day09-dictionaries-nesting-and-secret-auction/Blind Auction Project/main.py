#My completed version 07/17/2025
import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)

adding_participants = True
participant_bids = {}
while adding_participants:
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $ "))
    others = str(input("Are there any other bidders? Type 'yes' or 'no' \n")).lower()
    participant_bids[name] = bid
    if others == "yes":
        print("\n" * 20)
    else:
        adding_participants = False
        big_baller = max(participant_bids, key=participant_bids.get)
        big_pockets = participant_bids[big_baller]

        print(f"The winner is {big_baller} with a bid of ${big_pockets}")