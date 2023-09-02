# Print Odd Numbers: Create a program to print all odd numbers between 1 and N.

userInput = input("Input high-end to see all odd numbers: ")

userInput = int(userInput)

for num in range(1, (userInput + 1)):
    if num % 2 == 1:
        print(num)
    else:
        continue