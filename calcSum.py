# Calculate the Sum of Numbers: Create a program that calculates and prints the sum of all the numbers from 1 to N.

inputNumber = input("Enter a value for N: ")
inputNumber = int(inputNumber)

totalNum = 0

for num in range(0, inputNumber + 1):
    totalNum += num
print(totalNum)
