
# FUNCTIONS

def decimal_to_binary(decimal):    # This function converts decimal to binary

    if decimal == 0:
         print(0)
         return
    
    reminder_list = []

    while True:
        if decimal == 0:
            break
        
        reminder_list.append(decimal%2)
        decimal= int(decimal/2)
        

    reminder_list.reverse()

    print()
    for i in reminder_list:
        print(i, end="")

    print()    

    return



def binary_to_decimal(binary):    # This function converts binary to decimal
    binary_list = []
    binary_str_list = list(str(binary))

    for i in binary_str_list:
        binary_list.append(int(i))

    binary_list.reverse()
    

    decimal = 0
    idx = 0
    for i in (binary_list):
        
        decimal = decimal + (i * 2**idx)
        idx += 1

    print("\n" ,decimal)

    return





# MAIN CODE

while True:
    choice_input = int(input("What do you want ? (Decimal to binary = 1, Binary to decimal = 2) : "))
    # It takes input for user choice what user want

    if choice_input == 1:
            
        decimal_input = int(input("Please input your decimal number : "))   # It takes input of decimal
        decimal_to_binary(decimal_input)

    elif choice_input == 2:
        
        binary_input = int(input("Please input your binary number : "))   # It takes input of binary
        binary_to_decimal(binary_input)

    else:
        print("Please input valid number")
        continue
