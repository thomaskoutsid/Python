'''

Thomas Koutsidis

May 21st, 2022

Question 4

Write an interactive Python calculator program. 
This allows thr user to type a mathematical expression and print the value.
A for loop is included so the user can perform up to 100 calculations.

'''

def main():
    print("This is an interactive Python calculator!")
    for i in range(0, 100, 1):
        exp = eval(input("Enter an expression: "))
        print(exp)
    
main()    