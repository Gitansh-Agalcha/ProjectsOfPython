#Clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Simple Calcuator 

def add(a, b): #Addition
    return a + b

def sub(a, b): #Subtarction
    return a - b

def mul(a, b): #Multiplication
    return a * b

def div(a, b): #Divison
    return a / b 
    if(div != 0):
        print("Invalid")

print("Simple Calcutor")

num1 = float(int(input("Enter Your First Number:- "))) # User Num1
num2 = float(int((input("Enter Your Second Number:- ")))) # User Num2

print("Operation:- ")
print("1.Add \n2.Subtract  \n3.Multiply  \n4.Divide") # Options

choice = int(input("Enter Your choice = ")) #Choice Input to user

if(choice == 1): # choice = ADD
    print("Result = ", add(num1, num2))

elif(choice == 2): # choice = SUB
    print("Result = ", sub(num1, num2))

elif(choice == 3): # choice = MUL
    print("Result = ", mul(num1, num2))

elif(choice == 4): # choice = DIV
    print("Result = ", div(num1, num2))

else:
    print("Invalid Choice")

