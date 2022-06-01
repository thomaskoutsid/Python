'''
Thomas Koutsidis
May 21st, 2022

Question 1

This program prompts the user for a distance in kilometers.
It then converts and prints the distance in miles before terminating.

'''

def main():
    print("This program converts kilometers to miles")
    kilometers = eval(input("Enter the distance in kilometers: "))
    miles = kilometers * 0.62
    print("The distance is", miles, "miles.")
    
    
main()
