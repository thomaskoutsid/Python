'''
Thomas Koutsidis
May 29th, 2022

Question 3.1

This program asks a user for a positive integer (n) 
It then prints all numbers between 1 and n, inclusive, which are divisible by 3.
If the number is not positive, it will ask you to re-enter a valid integer.
'''
def main():
    print("This program prints the numbers divisible by 3.")
    number = eval(input("Enter a positive number: "))
    if number > 0:
        print("Numbers between 1 and", number, "divisible by 3 are: ")
        for x in range(1, number + 1):
            if x % 3 == 0:
                print(x)
    else:
        print("This number is not positive.\n")
        main()
        
main()
