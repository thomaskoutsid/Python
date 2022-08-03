'''
Thomas Koutsidis
July 1st, 2022

Question 3

The function to_letter_grade(score) that returns the letter grade for a scalar input "score".
The function main() reads file "score_headings.npy", calculates and prints the letter grade for each student.
'''

import numpy as np


def to_letter_grade(score):
    if score >= 0 and score < 60:
        return "F"
    elif score >= 60 and score < 66:
        return "D"
    elif score >= 66 and score < 70:
        return "D+"
    elif score >= 70 and score < 73:
        return "C-"
    elif score >= 73 and score < 76:
        return "C"
    elif score >= 76 and score < 80:
        return "C+"
    elif score >= 80 and score < 83:
        return "B-"
    elif score >= 83 and score < 86:
        return "B"
    elif score >= 86 and score < 90:
        return "B+"
    elif score >= 90 and score < 93:
        return "A-"
    elif score >= 93 and score <= 100:
        return "A"
    else:
        return


def main():
    letters = np.load("score_headings.npy")
    np.set_printoptions(suppress=True)
    identity = np.array(letters[:, 0])

    number = np.array(letters[: , 1:7].sum(axis = 1), dtype=float)
    score = np.around(number, decimals = 1)
    
    letter = []
    for i in score:
        i = to_letter_grade(i)
        letter.append(i)
     
    np.vectorize(to_letter_grade)

    final_score = np.array([identity, score, letter])
    final_scores = np.transpose(final_score)
    final_scores = final_scores.astype(str)

    
    print(final_scores)
    
   
    
main()