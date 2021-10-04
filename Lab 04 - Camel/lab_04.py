import random

def main():
    print("Welcome to Running from the cops!")
    print("You have stolen a police car and ran a red light")
    print("The cops are chasing you because they want their car back!")
    print("Survive your chase and out drive the cops.")

    done = False
    milesTraveled = 0
    copsTraveled = -20
    tiredness = 0
    gasStation = -1
    thirst = 0
    redBull = 4

    # User Options
    while not done:
        print("A. Full speed ahead.")
        print("B. Drink from Red Bull drink.")
        print("C. Moderate speed ahead.")
        print("D. Stop and refill car.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice?")

        # Check to see if want to quit
        if user_choice.lower() == "q":
            print("Goodbye Everyone!")

        # full speed ahead
        elif user_choice.lower() == "a":
            miles = random.randrange(10, 22)
            milesTraveled += miles
            thirst += 1
            tiredness += random.randrange(1, 5)
            copsTraveled += random.randrange(7, 15)
            gasStation = random.randrange(20)
            if gasStation == 10:
                thirst = 0
                tiredness = 0
                redBull = 4
                print("As you traveled you found a gas station!")
                print("You will fill car with gas and your body with RedBull!")
                print("Your car is ready to go.")
                print("The Cops keep on coming for you!!")
                print()
            else:
                print("You are moving forward at full speed, moving a total of", miles, "miles")
                print("you thirst continues to get worse!")
                print("Your car slowly keeps getting closer to on empty")
                print("Cop continue to chase you!")
                print()

        # Drink from RedBull
        elif user_choice.lower() == "b":
            if redBull > 0:
                redBull -= 1
                thirst = 0
                print("Take a refreshing drink!")
            else:
                print("Your redbull drink is gone! Your mouth is gonna be as dry as the Sahara Desert!")

         # Moderate speed
        elif user_choice.lower() == "c":
            miles = random.randrange(5, 14)
            milesTraveled += miles
            thirst =+ 1
            tiredness += 1
            copsTraveled += random.randrange(7, 15)
            gasStation = random.randrange(20)
            if gasStation == 10:
                thirst = 0
                tiredness = 0
                redBull = 4
                print("As you traveled you found a gas station")
                print("You will fill car with gas and your body with RedBull!")
                print("Your car is ready to go.")
                print("The Cops keep on coming for you!!")
                print()
            else:
                print("You are moving forward at moderate speed, moving a total of", miles, "miles")
                print("you thirst continues to get worse!")
                print("Your car slowly keeps getting closer to on empty")
                print("Cop continue to chase you!")
                print()

        # Rest and refill
        elif user_choice.lower() == "d":
            print("You stop for the night!")
            print("Car does not overheat.")
            print("Cops do not stop!")
            print()
            tiredness = 0
            copsTraveled += random.randrange(7, 15)

        # Status Check
        elif user_choice.lower() == "e":
            print("Miles traveled:", milesTraveled)
            print("Drink from RedBull:", redBull)
            print("Where cops are at:", milesTraveled - copsTraveled, "miles behind you.")
            print()

        elif user_choice.lower() == "q":
            print("Game Over!")

        # Updates on status
        # Thirst
        if thirst > 5:
            print("You have died of dehydration!")
            print("Game Over! Goodbye! :)")
            print()
            done = True
        elif thirst > 4:
            print("Chug some RedBull!")

        if not done:
            # Distance traveled and win check
            if milesTraveled >= 200:
                print("Congrats! You have out ran the cops!")
                print("You have Won!")
                print()

        if not done:
            # Tiredness
            if tiredness > 9:
                print("You have died sleep of exhaustion!")
                print("With no energy you will be caught by the cops!")
                print("Game Over! Goodbye! :)")
                print()
                done = True
            elif tiredness > 6:
                print("You are tired.")
                print()

        if not done:
            # Cops Distance from you
            if milesTraveled - copsTraveled <= 0:
                print("The Cops have caught up tp you!")
                print("They will arrest you and take their car back.")
                print("Game Over! Goodbye! :)")
                print()
                done = True
            elif milesTraveled - copsTraveled < 15:
                print("You can see the cops! Keep running!")
                print("The cops are getting closer to capturing you!")
                print()

    print("Goodbye! :)")
main()

