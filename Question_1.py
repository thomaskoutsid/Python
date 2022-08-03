'''
Thomas Koutsidis
June 12th, 2022

Question 1

This program has the definition of two functions.
1. sum_n(n) - this returns the sum of the first n positive integers.
2. sum_cubes(n) - this returns the sum of the cubes of the first n positive integers.
The main() prompts the user for a positive integer n. It then calls the above functions.
It prints out the sum of the first n integers and the sum of the cubes of the first n integers.

'''

def sum_n(n):
    sumOfN = 0
    for num in range(n + 1):
        sumOfN = sumOfN + num
    return sumOfN


def sum_cubes(n):
    sumOfCubes = 0
    for num in range(n + 1):
        cube = num ** 3
        sumOfCubes = sumOfCubes + cube
    return sumOfCubes


def main():
    print("This program calculates the sum of the first n numbers and the sum of their cubes.")
    num_input = int(input("Please enter a positive integer: "))
    if num_input < 1:
        print("This integer is not positive.")
        return
    
    sum_n_print = sum_n(num_input)
    sum_cubes_print = sum_cubes(num_input)
    
    print("The sum of the first", num_input, "integers is", sum_n_print)
    print("The sum of cubes of the first", num_input, "integers is", sum_cubes_print)

    
main()