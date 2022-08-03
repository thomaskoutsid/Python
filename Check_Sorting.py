'''
Thomas Koutsidis
June 24th, 2022

Question 2

The main() function prompts the user for a sequence of numbers in a single line, separated by spaces, and calls the functions below to determine if the numbers are ordered or same.
It then prints "The numbers are in ascending order," "the numbers are the same," "the numbers are in descending order," or "the numbers are not sorted." 
The function checks for special cases and prints: "Error! No input number," or "You entered a single number" based on what was input.
The following functions are called to determine the order:
- to_numbers(nums): modifies each element of the list of strings nums by converting it to numbers. This uses exception to catch non-numbers and prints an error message.
- is_ascend(nums): returns True if the numbers in the list nums are in ascending order and False otherwise.
- is_descend(nums): returns True if the numbers in the list nums are in descending order and False otherwise.
- are_same(nums): returns True if the numbers in the list nums are the same and False otherwise.

'''

def to_numbers(nums):
    for i in nums:
        try:
            nums = int(i)
        except ValueError:
            return False
    

def is_ascend(nums):
    flag = True
    for i in range(1, len(nums) - 1):
        x = nums[i - 1]
        y = nums[i]
        if x > y:
            flag = False
        elif x < y:
            flag = True
    return flag
    


def is_descend(nums):
    flag = True
    for i in range(1, len(nums) - 1):
        x = nums[i - 1]
        y = nums[i]
        if y > x:
           flag = False
        elif y < x: 
            flag = True
    return flag
        
        
def are_same(nums):
    flag = True
    for i in range(1, len(nums) - 1):
        x = nums[i - 1]
        y = nums[i]
        if y != x:
            flag = False
        elif y == x:
            flag = True
    return flag
        
    
    
def main():
    print("This is a program to check if the input numbers are sorted.")
    num_input = input("Enter the numbers separated by a space: ")
    nums = num_input.split(" ")
    to_numbers(nums)
    is_ascend(nums)
    is_descend(nums)
    are_same(nums)
    if nums[0] == "":
        print("Error! No input number.")
        return
    elif to_numbers(nums) == False:
        print("Error! The input is not a number! ")
        return
    elif (len(nums) == 1):
        print("You entered a single number.")
        return
    else:
        if is_ascend(nums) == True:
            print("The numbers are in ascending order.")
        elif is_descend(nums) == True:
            print("The numbers are in descending order.")
        elif are_same(nums) == True:
            print("The numbers are the same.")
        else:
            print("The numbers are not sorted.")
    
       
main()
