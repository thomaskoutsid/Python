'''
Thomas Koutsidis
June 2nd, 2022

Question 3

This program calculates the numeric value of a single name(in lowercase letters) provided as input.
Ex. 'a' = 1, b = '2', c = '3'. abc = 1 + 2 + 3 = 6
'''

def main():
    print("This program computes the value of a string.")
    name = input("Enter any name in lowercase: ").lower()
    sumOfName = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in name:
        sumOfName = alphabet.find(i) + sumOfName
    print("The numberic value of this name is:", sumOfName)
    

main()