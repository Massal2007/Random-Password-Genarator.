import random
import array 
from time import sleep

print("Welcome to password generator!")

while True:

    max_len = int(input("\nEnter the length of your password\nMinimum length is 4 charactres\nLength: "))

    lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

    uppercase_characters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']


    all_characters = lowercase_characters + uppercase_characters + num + symbols

    random_digit = random.choice(num)
    random_symbol = random.choice(symbols)
    random_upper = random.choice(uppercase_characters)
    random_lower = random.choice(lowercase_characters)

    temp_pass = random_digit + random_symbol + random_upper + random_lower

    for x in range(max_len - 4):
        temp_pass = temp_pass + random.choice(all_characters)
        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    password = ""

    for i in temp_pass_list:
        password = password + i

    sleep(2)
    
    print("Your password is: ", password)
    
    sleep(2)

    resume = str(input("\nDo you want to create a new one password?Hit enter to continue or [n] to stop\nContineu? "))


    if resume == "n":
        sleep(2)
        break
    
    else:
        sleep(2)







    
