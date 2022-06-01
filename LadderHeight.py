'''
Thomas Koutsidis
May 29th, 2022

Question 2

This program determines the length of a ladder (in feet) that is required to reach a given height when leaned against a house.
It prompts the user for the height in feet and the angle in degrees of the ladder.
The answer is then rounded to 2 decimal points.
'''
import math

def main():
    print("This program calculates the length of a ladder.")
    height = float(input("Enter the height in feet: "))
    angle = float(input("Enter the angle in degrees: "))
    radians = (math.pi / 180) * angle
    length = height / math.sin(radians)
    print("The length of the ladder is", round(length, 2), "feet.")
    
    
main()
    
    
    
