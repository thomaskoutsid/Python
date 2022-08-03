'''
Thomas Koutsidis
June 25th, 2022

Question 4

The main() function prompts the user for positive integers lower_limit and upper_limit.
It calls the function print_prime(lower_limit, upper_limit) to print prime numbers in the interval.
The main() prints error messages in case the entered numbers are not positive or if upper_limit < lower_limit.
The function is_prime(n) takes a positive integer n as an input parameter and returns True if n is a prime number and False otherwise.
The print_prime(lower_limit, upper_limit) prints all prime numbers between the limits (inclusive).
'''

def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
    return prime


def print_prime(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit + 1):
        if is_prime(i):
            print(i)
            

def main():
    print("This program prints prime numbers in a range.")
    
    lower_limit = input("Enter the lower limit of a range: ")
    try:
        lower_int = int(lower_limit)
    except ValueError:
        print("Error! You entered a non-integer!")
        return
    if lower_int <= 0:
        print("Invalid input: Lower limit should be a positive integer.")
        return
   
    upper_limit = input("Enter the upper limit of a range: ")
    try:
        upper_int = int(upper_limit)
    except ValueError:
        print("Error! You entered a non-integer")
        return
    if upper_int <= 0:
        print("Invalid input: Upper limit should be a positive integer.")
        return
    if lower_int > upper_int:
        print("Invalid input: Upper limit is less than lower limit.")
        return
    if lower_int == upper_int:
        print("Invalid input: Your limits are the same number.")
        return
    
    print_prime(lower_int, upper_int)
   
    
main()