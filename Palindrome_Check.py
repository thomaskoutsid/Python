'''
Thomas Koutsidis
June 2nd, 2022

Question 4

This program prompts the user for a string.
It then determines if the string is a palindrome.
It then prints where or not it is a palindrome.
'''
def main():
    print("This program checks if an input string is a palindrome.")
    palindrome = input("Enter a string: ")
    if palindrome == palindrome[::-1]:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome")
            
main()
