'''
Thomas Koutsidis
June 24, 2022

Question 1

A sentinel loop is used to write a program that prompts the user to enter a sequence of numbers.
It then prints: total count of numbers entered, smallest number entered, largest number entered, count of positive numbers and count of negative numbers.
The loop terminates when the user enters an empty string. 
The program uses exception to catch if the user enters a non-number and prints an error and continues execution.

'''

def main():
    print("This program prints min, max and count of positive and negative numbers.")
    numbers = []
    
    while True:
       
        number = input("Enter a number: ")
        if number == "":
            break
        
        
        try: 
            number_float = float(number)
            numbers.append(number_float)
        except ValueError:
            print("Error! Please enter a valid number: ")
            
    count = 0
    min = numbers[0]
    max = numbers[0]
    pos_count = 0
    neg_count = 0
    
    for num in numbers:
        
        count = count + 1
        
        if num < 0:
            neg_count = neg_count + 1
        elif num > 0:
            pos_count = pos_count + 1
            
        if min > num:
            min = num
        if max < num:
            max = num
            
    print("You have entered", count, "numbers.")
    print("The smallest number is", min)
    print("The largest number is", max)
    print("There are", pos_count, "and", neg_count, "negative number(s).")
    

main()
    
    
