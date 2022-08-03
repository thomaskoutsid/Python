'''
Thomas Koutsidis
June 16th, 2022

Question 2

The program has a function called body_mass_index(height, weight) which receives height in inches and weight in pounds.
It then converts height to meters and weight to kilograms, and then calculates and returns the BMI.
The main() function prompts for a person's height (inches) and weight (pounds), and calls the body_mass_index(height, weight) function to determine the BMI.
It prints the BMI and a message telling the person where they stand (above, within, or below the healthy range).
The main() function uses exception to check if the user enters a non-number. It prints a message and quits if the user enters a non-number or negative number.
'''

def body_mass_index(height, weight):
    height_m = height * 0.0254
    weight_kg = weight * 0.45
    bmi = weight_kg / (height_m ** 2)
    if bmi >= 19 and bmi <= 25:
        print("You are within the healthy range.")
    elif bmi < 19:
        print("You are below the healthy range.")
    else:
        print("You are above the healthy range.")
    return bmi

    
def main():
    print("This program calculates body mass index.")
    
    height = input("Enter your height in inches: ")
    try:
        height = float(height)
    except ValueError:
        print("Error! You entered a non-number.")
        return
    if (height < 0):
        print("Error! You entered a negative number!")
        return
    weight = input("Enter your weight in pounds: ")
    try:
        weight = float(weight)
    except ValueError:
        print("Error! You entered a non-number")
        return
    if (weight < 0):
        print("Error! You entered a negative number!")
        return
    
    your_bmi = body_mass_index(height, weight)
    print("Your BMI is", your_bmi)
    
    
main()
    