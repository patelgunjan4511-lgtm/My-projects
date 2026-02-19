import random

def decode(code_word):

    if len(code_word)<=2:
        decode_word = code_word[::-1]
        print(f"\n decoded word is \"{decode_word}\"")

        return

    else:
        decode_word = code_word[-4]+code_word[3:-4]
        print(f"\n decoded word is \"{decode_word}\"")

        return

def send(code_word):

    print("\n"+code_word)

    print("\n You want to decode it so press 1 otherwise press 0 : ", end="")
    i = int(input())

    if i == 1:
        decode(code_word)
        return

    else:
        return

i = input("Enter your word : ")

chars = "abcdefghijklmnopqrstuvwxyz"

if " " in i:
    raise("Enter the word, sentenses are not allowed")

if len(i) < 3:
    code_word = i[::-1]

else:
    f_choise = random.choice(chars)
    s_choise = random.choice(chars)
    t_choise = random.choice(chars)
    ff_choise = random.choice(chars)
    fs_choise = random.choice(chars)
    ft_choise = random.choice(chars)
    s_append = f_choise + s_choise + t_choise
    e_append = ff_choise + fs_choise + ft_choise

    code_word = s_append + i[1:] + i[0] + e_append
    
print("\n The code word is " + code_word)
print("\n \n You want to send it so press 1 otherwise press 0 : ", end="")
i = int(input())

if i == 1:
    send(code_word)

    
