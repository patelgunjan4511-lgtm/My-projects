import random


number = random.randint(1,101)
print("Guess the number between 1 to 100 \n")

while True:
    
    user_number = int(input("Enter your number : "))

    if user_number > 100 or user_number < 1:
        print("Number is Invelid !")
        continue

    if user_number > number:
        print("Number is greater")

    elif user_number < number:
        print("Number is lesser")

    else:
        print(f"Congratulations ! You have pridict correctly, the right number is {number} !")

    

    