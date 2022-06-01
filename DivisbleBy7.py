'''
Thomas Koutsidis
May 29th, 2022

Question 3.2

This program asks the user for a positive integer, n.
It uses the counter pattern to find out and print the count of all numbers between 1 and n, inclusive, which are divisble by 7.
Using an if and else statement, I had the program reset if the number was not positive.
'''
def main():
    print("This program prints the count of numbers divisble by 7.")
    number = eval(input("Enter a positive integer: "))
    if number > 0:
        count = 0
        for x in range(1, number + 1):
            if x % 7 == 0:
                count = count + 1
        print("There are", count, "numbers between 1 and", number, "that are divisible by 7.")
    else:
         print("This number is not positive.")
         main()


main()
