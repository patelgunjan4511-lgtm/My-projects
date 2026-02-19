import random

computer_choices_item = ("Rock", "Paper", "Scissor")
computer_choices = (1, 2, 3)

while True:
    computer_choice = random.choice(computer_choices)

    play_choice = int(input("\n You want to play this game (Yes = 1, No = 0) : "))

    if play_choice == 0:
        break

    if play_choice > 1 or play_choice < 0:
        print("\n Please input valid number")
        continue

    your_choice = int(input("\n Rock = 1, paper = 2, scissor = 3, so choose one : "))

    if your_choice > 3 or your_choice < 1:
        print("\n Please input valid number")
        continue

    who_wins = computer_choice - your_choice

    if who_wins == -1 or who_wins == 2:
        print(f"\n you wins computer choice is {computer_choices_item[computer_choice-1]}")

    elif who_wins == 0:
        print(f"\n This is tie computer choice is {computer_choices_item[computer_choice-1]}")

    else:
        print(f"\n computer wins computer choice is {computer_choices_item[computer_choice-1]}")
                