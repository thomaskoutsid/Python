'''
Thomas Koutsidis
May 29th, 2022

Question 5

This program prompts the user for two positive integers, start and end.
Start and end define a range of numbers including both start and end.
The program calculates and prints the ratio of the sum of even numbers to the sum of all the numbers in the range.
It is rounded to three decimal places.
'''
def main():
    start = eval(input("Enter the starting number of a range: "))
    end = eval(input("Enter the ending number of a range: "))
    even = 0
    total_sum = 0
    for x in range(start, end+1):
        if x % 2 == 0:
            even = even + x
    for x in range(start, end+1):
        total_sum = total_sum + x
    ratio = even / total_sum
    print("The ratio of sum of even numbers to sum of all numbers in this range is", round(ratio, 3))
    

main()
        
