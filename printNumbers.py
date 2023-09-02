# Print Numbers from 1 to N: Write a program that prints numbers from 1 to N, where N is a user-defined integer.

userInput = input("Please input high-end value: ")
#user input comes in as a string so you have to convert it to an integer value
userInput = int(userInput)

for num in range(1, (userInput + 1)):
    print(num)