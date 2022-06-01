'''

Thomas Koutsidis
May 21st, 2022

Question 2

This program prompts the user for mpg of a vehicle.
It then calculates it and prints the fuel consumption in liters per 100 km.

Important conversions:
1 mi = 1.6 km
1 gallon = 3.785 liters

'''


def main():
    print("This program converts mileage to liters per 100 km.")
    miles = eval(input("Enter the milage (miles per gallon): "))
    miles_to_km = miles * 1.6
    gallon_to_liters = 100 * 3.785
    liters_per_km = gallon_to_liters / miles_to_km
    print ("The vehicle fuel economy is", miles, "per gallon.")
    print("The vehicle fuel consumption is", liters_per_km, "liters per 100 km.")
    
   
main()
                 

