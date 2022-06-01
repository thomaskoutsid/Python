'''
Thomas Koutsidis
May 29th, 2022

Question 1

This program prompts the user for the temperate in Fahrenheit.
It then prompts the user for thr wind speed in miles per hour.
Then, it calculates and prints the wind chill.
The wind chill is rounded to one digit after the decimal point.
'''
import math

def main():
    print("This program calculates the wind chill.")
    temp = float(input("Enter the temperature in degrees Fahrenheit: "))
    wind = float(input("Enter the wind speed in miles per hour: "))
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * math.pow(wind, 0.16) + 0.4275 * temp * math.pow(wind, 0.16)
    print("The wind chill index is", round(wind_chill, 1))
    
    
main()
