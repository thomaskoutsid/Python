'''
Thomas Koutsidis
June 12th, 2022

Question 2

The function print_X(n,c) prints the letter X in n lines using the character c.
n is a positive and odd integer.
'''

def print_X(n, c):
    for i in range(n):
        for j in range(n):
            if (i == j) or ((n - j - 1) == i):
                print(c, end = " ")
            else:
                print(" ", end = " ")
        print(" ")


def main():
    print("This program prints the letter X using the character of your chooice.")
    n = int(input("Enter a positive odd integer: "))
    if n < 1:
        print("This integer is not positive.")
        return
    if n % 2 == 0:
        print("This integer is even.")
        return
    c = input("Enter a character: ")
   
    print_X(n,c)
    
main()