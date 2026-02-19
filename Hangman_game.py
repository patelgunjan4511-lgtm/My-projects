import random

def alph_in_word(word, ans):

    if ans in word:
        return 1
    
    else:
        return 0

hangmans = (
    
"""
________
|       |
|
|
|
|
        """,
"""
________
|       |
|       0
|       |
|
|
""",
"""
________
|       |
|       0
|      /|
|
|
""",
"""
________
|       |
|       0
|      /|\\
|
|
""",
"""
________
|       |
|       0
|      /|\\
|      / 
|
""",
"""
________
|       |
|       0
|      /|\\
|      / \\
|
"""

)

words = (
    "apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry", "pineapple",
    "mango", "kiwi", "melon", "peach", "plum", "cherry", "lemon", "lime", "coconut"
)

while True:

    word = random.choice(words)

    your_guess = []

    for i in word:

        your_guess.append("_")

    idxes = 0

    while True:

        print("The words are : ")
        for i in words:
            print(i, end=" ")
        print()
        print()

        if idxes == 6:
            print("\n You lose ! \n")
            break

        if "_" not in your_guess:
            print(f"\n {word}")
            print("\n You won ! \n")
            break

        for i in (your_guess):
            print(f"{i} ", end="")


        ans = input("\n \n Enter your answer : ")

        if len(ans) > 1:
            print("\n Enter the alphabet, word or sentenses are not allowd \n")
            continue

        if ans in your_guess:
            print("\n You have already inputed this alphabet please try different \n")
            continue

        
        if ans in word:
            idx = 0
            for i in word:
                
                if i == ans:
                    your_guess[idx] = i
                    idx += 1

                else:
                    idx += 1
                    
        else:
            print(hangmans[idxes])
            idxes += 1
