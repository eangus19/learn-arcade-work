import random

def main():
    print("Welcome to Running from the cops!")
    print("You have stolen a police car and ran a red light")
    print("The cops are chasing you because they want their car back!")
    print("Survive your chase and out drive the cops.")

    done = False
    while not done:
        print("A. Full speed ahead.")
        print("B. Drink from Red Bull drink.")
        print("C. Moderate speed ahead.")
        print("D. Stop and refill car.")
        print("E. Status check.")
        print("F. Quit.")

    user_choice = input("What is your choice?")
    if user_choice.lower() == "q":
        done = True
        print("Goodbye Everyone!")

    elif user_choice.lower() == "a":
        done = True
        print("Go! Go! GO!")

    elif user_choice.lower() == "b":
        done = True
        print("Chug! Chug! Chug!")

    elif user_choice.lower() == "c":
        done = True
        print("Keep on going!")

    elif user_choice.lower() == "d":
        done = True
        print("Rest and refill on gas!")

    elif user_choice.lower() == "e":
        done = True
        print("Where are we at? Here is the info!")

    elif user_choice.lower() == "f":
        done = True
        print("Game Over!")

main()

