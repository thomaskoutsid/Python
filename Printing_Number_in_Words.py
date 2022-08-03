'''
Thomas Koutsidis
June 2nd, 2022

Question 2

This program takes a positive integer number from the user.
It prints the number in words.
'''
def main():
   num = input("Enter a positive number: ")
   print("The number you typed is:", num)
   nList = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
   print("This number in words is:")
   for n in num:
       print(nList[int(n)], end = " ")
       
main()
