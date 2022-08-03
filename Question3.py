'''
Thomas Koutsidis
June 24th, 2022

Question 3

The main() calls the three functions listed below and prints the sum of rows of the input matrix.
The three functions are:
- in_matrix(): prompts the user for dimensions m and n of a matrix and gets the integers from the user, which are elements of the matrix. 
It then builts and returns a nested list mx with m elements, each element is a list of n integers. 
List mx represenets an (m x n) matric with integer elements. The program crashes if the user inputs a non-integer.
- print_matrix(mx): prints the elements of matrix mx row by row.
- sum_rows(mx): returns a list with elements that are the sums of numbers in mx rows.

'''

def in_matrix():
    print("Program to sum the rows of an input matrix.")
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    mx = []
    for i in range(m):
        row = []
        for j in range(n):
            print("Enter next element of row", i, end = ": ")
            num = int(input())
            row.append(num)
        mx.append(row)
    return mx


def print_matrix(mx):
    print("Input matrix: ")
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            print(mx[i][j], end = "\t")
        print()


def sum_rows(mx):
    sums = []
    for i in range(len(mx)):
        sum = 0
        for j in range(len(mx[0])):
            sum = sum + mx[i][j]
        sums.append(sum)
        print("Sum of numbers in row", i, "is", sum)
        
    
def main():
    mx = in_matrix()
    print_matrix(mx)
    sum_rows(mx)
    
    
main()
    
    