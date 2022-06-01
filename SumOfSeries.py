'''
Thomas Koutsidis
May 29th, 2022

Question 4

This program sums a series of numbers entered by the user.
It prompts the user for how many numbered to be summed.
It inputs each one of the numbers and prints a total sum.
'''
def main():
    sum = 0
    print("This program calculates the sum of numbers entered by the user.")
    number = eval(input("Enter the amount of numbers you want to sum up: "))
    for x in range(number):
        digits = eval(input("Enter the next number: "))
        sum = sum + digits
    print("The sum of the", number, "numbers is", sum)
        

main()
