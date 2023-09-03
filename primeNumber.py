# Check for Prime Numbers: Create a program that checks if a given number is prime or not.
# Prime numbers are natural numbers that are divisible by only 1 and the number itself.


def main():
    userInput = input("Enter a number to see if its PRIME: ")
    convertInput = int(userInput)

    isPrime = isPrimeNumber(convertInput)

    if isPrime:
        print(f"{convertInput} is a Prime number.")
    else:
        print(f"{convertInput} is not a Prime number.")

    
        
def isPrimeNumber(n):
    if n <= 1:
        return False

    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    
    return True


main()
