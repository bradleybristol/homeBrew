# Print Even Numbers: Write a program to print all even numbers between 1 and N.

userInput = input("Enter top-end to see even numbers to n: ")

userInput = int(userInput)

for num in range(1, (userInput + 1)):
    if num % 2 == 0:
        print(num)  
    else:
        continue
