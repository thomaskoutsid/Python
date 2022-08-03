'''
Thomas Koutsidis
June 12th, 2022

Question 4

This program has the following functions: square_each(nums), sum_list(nums) and to_numbers(str_list).
square_each(nums), nums is a list of numbers. It modifies the list nums by squaring each entry.
sum_list(nums), nums is a list of numbers. It returns the sum of the numbers in the list.
to_numbers(str_list), str_list is a list of strings. Each string represents a number. It modifies each string in the list by converting it to a number.
The main() uses these functions to compute the sum of the squares of numbers in each line in a file.
The file contains several lines and each line contains numbers separated by spaces.
The main() prompts for a file name and prints out the sum of the squares of the numbers in each line in the file.
'''

def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums[i]


def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum

        
def to_numbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])
    return float(str_list[i])

        
def main():
    print("This program prints the sum of squares of each line in a file.")
    file_name = input("Enter the name of file with numbers: ")
    infile = open(file_name, "r")
    sumInLine = 1
    for i in infile:
        line = list(i.split())
        to_numbers(line)
        square_each(line)
        num = sum_list(line)
        print("The sum of square in line", sumInLine, "is", num)
        sumInLine = sumInLine + 1
    infile.close()
    

main()