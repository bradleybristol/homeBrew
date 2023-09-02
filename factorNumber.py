# Factorial of a Number: Write a program that calculates the factorial of a given number N using a for loop.


def loopFactor(n):
    result = 1              # because 0! = 1 by definition
    for i in range(1, n+1):
        result *= i         # multiply result by current value of i
    return result           # return result for next iteration

def main():
    toFactor = int(input("Enter a number to find factorial: "))
    printFactor = loopFactor(toFactor)
    print(f"The factorial of {toFactor} is: {printFactor}")
    

main()