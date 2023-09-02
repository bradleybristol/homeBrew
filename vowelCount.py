# Count Vowels in a String: Implement a program that counts the number of vowels (a, e, i, o, u) in a given string.

userString = input("Type in a string to have the vowels counted :")

# good practice getting used to working with functions

# function, the main program
def main():
    totalVowels = vowelCount(userString)
    print(totalVowels)

# function, counting the vowels
def vowelCount(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU": # i had char == "a", char == "e", etc, but i found out how to simplify with the 'in' operator
            count += 1
    return count

main()