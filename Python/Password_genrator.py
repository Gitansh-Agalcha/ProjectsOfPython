#Clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Password Genrator
import random
import string

length = int(input("Enter Your Password Length:- "))

char = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

Password = "".join(random.choice(char) for i in range(length))

print("Your Password is:",Password)


