'''
Thomas Koutsidis
June 15th, 2022

Question 1

This program has a function called letter_grade(score) that receieves a score and calculates and returns that score as its corresponding letter grade.
The main() function prompts the user for the score. The exception is to check if the user enters a string that is not a number. IF the user enters a non-number or a number outside of 0-100, the main() prints a message and terminates.
The main() function calls letter_grade to convert the score into a letter grade and prints it.

'''

def letter_grade(score):
    if score >= 0 and score <= 59.99:
        return "F"
    elif score >= 60 and score <= 65.99:
        return "D"
    elif score >= 66 and score <= 69.99:
        return "D+"
    elif score >= 70 and score <= 72.99:
        return "C-"
    elif score >= 73 and score <= 75.99:
        return "C"
    elif score >= 76 and score <= 79.99:
        return "C+"
    elif score >= 80 and score <= 82.99:
        return "B-"
    elif score >= 83 and score <= 85.99:
        return "B"
    elif score >= 86 and score <= 89.99:
        return "B+"
    elif score >= 90 and score <= 92.99:
        return "A-"
    elif score >= 93 and score <= 100:
        return "A"
    else:
        return "an error! The total score must be between 0 and 100, rounded to two decimals."


def main():
    print("This program calculates the letter grade from a total score.")
    score = input("Enter your total score: ")
    
    try: 
        score = float(score)
        
    except ValueError:
        print("Error! You entered a string that is not a number!")
        return
        
    if (score < 0) or (score > 100):
        print("Error! The total score must be between 0 and 100.")
        return
    
    your_grade = letter_grade(score)
    print("Your letter grade is", your_grade)
    

main()