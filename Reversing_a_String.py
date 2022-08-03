'''
Thomas Koutsidis
June 2nd, 2022

Question 1

This program takes an input string from the user.
It prints the string in reverse order by using indexing and slicing.
'''
def main():
    print("This program prints a string in reverse order.")
    reverse = input("Enter a string: ")
    print("The string you entered was:", reverse)
    print("This string in reverse order is", reverse[::-1])
    
    
main()
