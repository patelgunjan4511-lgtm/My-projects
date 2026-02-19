import random

words = (
    "apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry", "pineapple",
    "mango", "kiwi", "melon", "peach", "plum", "cherry", "lemon", "lime", "coconut"
)

word = random.choice(words) 
user_l = []

for i in word:
    user_l.append("_")


tries = 0

print("These are words : ")
print()

for i in words:
    print(i, end = " , ")

print()
print()
while True:

    for i in user_l:

        print(i,end=" ")

    print()

    if tries == 10:
        print()
        print("You lose")
        print()
        break

    if "_" not in user_l:
        
        print("You won")
        print()
        break
    

    inp = input("\n What is your guess : ")[0]
    print()
    
    for i in range(len(word)):
        if inp in word[i]:
    
            user_l[i] = word[i]

    tries = tries+1
