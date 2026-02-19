from random import choice

def want_play():

    choice_for_play = int(input("You want to play ? (Yes = 1, No = 0 ) : "))    # Takes input for play next game


    return True if choice_for_play == 1 else False

def choice_for_first_chance():

    choice_for_take_first_chance = int(input("You want to take first chance ? (Yes = 1, No = 0 ) : "))    # Takes input for first chance

    return True if choice_for_take_first_chance == 1 else False

def your_chance():

    input_of_user_number = int(input("Enter number between 1 and 3 : "))    # This takes user input for number
    
    return input_of_user_number

def computer_chance():

    if sum_of_numbers >= 18 and sum_of_numbers != 20:
        computer_choice = choice(1,2)

    elif sum_of_numbers == 20:
        computer_choice = 1

    else:
        computer_choice = choice(num)

        print(f"Computer added {computer_choice}")


    return computer_choice

num = (1,2,3)   # This is touple of number which computer will take

sum_of_numbers = 0  # This adds computer inputs and user inputes

while True:

    if sum_of_numbers >= 21:
        
        want_play()     # This function takes input for play choice

        if want_play == False:  # If want to play is no means 0 so function returns false and it will braak loop
            break

        else:
            sum_of_numbers = 21

    if sum_of_numbers == 0 or sum_of_numbers >= 21:

        if choice_for_first_chance():   # If choice_for_first_chance function returns true means user want to take first chance

            sum_of_numbers += your_chance()
            print(sum_of_numbers)

    
    sum_of_numbers += computer_chance()
    print(sum_of_numbers)

    if sum_of_numbers >= 21:    # If number has became 21 or greater so it will not exicute next code

        print("You win computer lose")
        continue

    sum_of_numbers += your_chance()
    print(sum_of_numbers)

    if sum_of_numbers >= 21:    # If number has became 21 or greater so it will not exicute next code

        print("You lose computer win")
        continue
