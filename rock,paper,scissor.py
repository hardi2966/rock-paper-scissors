import random

options = ["Rock", "Paper", "Scissors"]

machine_score = 0
user_score = 0

while True:
    machine = random.choice(options)

    user = input("Rock, Paper or Scissors? (Type 'End' to quit): ").capitalize()

    if user == machine:
        print("Tie!")

    elif user == "Rock":
        if machine == "Paper":
            print("You lose!", machine, "covers", user)
            machine_score += 1
        else:
            print("You win!", user, "smashes", machine)
            user_score += 1

    elif user == "Paper":
        if machine == "Scissors":
            print("You lose!", machine, "cut", user)
            machine_score += 1
        else:
            print("You win!", user, "covers", machine)
            user_score += 1

    elif user == "Scissors":
        if machine == "Rock":
            print("You lose!", machine, "smashes", user)
            machine_score += 1
        else:
            print("You win!", user, "cut", machine)
            user_score += 1

    elif user == "End":
        print("\nFinal Scores:")
        print(f"Computer's score is: {machine_score}")
        print(f"Your score is: {user_score}")
        break

    else:
        print("Invalid input! Please enter Rock, Paper, Scissors or End.")