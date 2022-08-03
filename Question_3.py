'''
Thomas Koutsidis
June 12th, 2022

Question 3

factorial(m) calculates the factorial of a positive integer n.
main() uses factorial(m) to calculate the number of combinations of n objects taken r objects at a time.
The formula that calculates the number of combinations is: C(n,r) = n! / (r! * (n - r)!)
'''

def factorial(m):
    factorial_m = 1
    for n in range(1, m + 1):
        factorial_m = factorial_m * n
    return factorial_m


def main():
    print("This program calculates the number of combinations of n objects taken r at the time.")
    n = int(input("Enter a positive integer for n: "))
    r = int(input("Enter a positive integer for r: "))
    if n < 1:
        print("The integer n is not positive.")
        return
    if r < 1:
        print("The integer r is not positive.")
        return
    if n < r:
        print("Error! Number n is less than r!")
        return
    
    factorial_n = factorial(n)
    factorial_r = factorial(r)
    factorial_n_r = factorial(n - r)
    combination = factorial_n / (factorial_r * factorial_n_r)
    
    print("Number of combinations C(", n, ",", r, ") = ", combination)
    
    
main()
    
