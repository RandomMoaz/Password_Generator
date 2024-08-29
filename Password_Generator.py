import string 
import random

L1 =list(string.ascii_uppercase)
L2 =list(string.ascii_lowercase)
L3 =list(string.digits)
L4 =list(string.punctuation)

Characters_number = input("How many characters do you want in your password? :")

while True:
    try:
        Characters_number =int(Characters_number)
        if Characters_number <6 :
            print("You need more than 6 characters in your password ")
            Characters_number=input("Please enter the number again")
        else:
            break     
    except:
        print("Please enter number only ")
        Characters_number=input(" Pleasw Enter How many characters do you want in your password: ")

random.shuffle(L1)
random.shuffle(L2)
random.shuffle(L3)
random.shuffle(L4)

part1 = round(Characters_number * (30/100))
part2 = round(Characters_number * (20/100))

password =[]

for i in  range(part1):
    password.append(L1[i])
    password.append(L2[i])

for i in range(part2):
    password.append(L3[i])
    password.append(L4[i])

random.shuffle(password)    

password ="".join(password[0:])

print( f"Here is yor password: {password}")
