# higher lower logo and the vs logo are always stay on screen
#  import random number
from random import choice
from Game_Of_data import data
from arts import logo, vs
import os

print(logo.__doc__)


def format_data(account):
    # Takes  the account data and return the  printable format.
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_des} from {account_country}"


def check_answer(guess, x_follower, y_follower):
    """Take the user guess and follower count and returns if thet got it right."""
    if x_follower > y_follower:
        return guess == "x"
    else:
        return guess == "y"


score = 0
account_y = choice(data)

while True:
    # Generate account and making account at position Y
    # to become  the  next account at position  x
    account_x = account_y
    account_y = choice(data)
    while account_x == account_y:
        account_y = choice(data)
    print(f"Compare X: {format_data(account_x)}.")
    print(vs.__doc__)
    print(f"Against Y: {format_data(account_y)}.")

    # Ask user for guess
    guess = input("who has more follower? Type 'X' or 'Y': ").lower()

    # check if user is correct and get follower count of each account.
    x_follower_account = account_x["follower_count"]
    y_follower_account = account_y["follower_count"]
    is_correct = check_answer(guess, x_follower_account, y_follower_account)
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Display art
    print(logo.__doc__)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. final score: {score}")
        break
