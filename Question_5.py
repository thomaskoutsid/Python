'''
Thomas Koutsidis
June 12th, 2022

Question 5

The function count_digits(line) counts and returns the number of digits in a string line.
The main() prompts the user for the name of a text file and uses the previous function to count and print the total number of digits in each line of the text file.
'''

def count_digits(line):
    count = 0
    for c in line:
        if c.isdigit():
            count = count + 1
    return count


def main():
    print("This program prints the number of digits in each line of a file.")
    file_name = input("Enter the name of the input text file: ")
    infile = open(file_name, "r")
    line_num = 0
    for lines in infile:
        line_num = line_num + 1
        num = count_digits(lines)
        print("There are", num, "digits in line", line_num) 
    infile.close()
        

main()