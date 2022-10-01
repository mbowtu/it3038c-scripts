#guess the number game'
import random

print("Enter a number between 0-10")
userInput = int(input())
numb = random.randint(0, 10)
while userInput != numb :
    if userInput < numb :
        print("The number is higher. Please enter a new number:")
        userInput = int(input())
    elif userInput > numb :
        print("The number is lower. Please enter a new number:")
        userInput = int(input())
    else:
        print("good guess:")

print("You have guess the righ number: " + str(int(numb))+ " congratulation!!")
