'''
Thomas Koutsidis
July 1st, 2022

Question 1

This program uses NumPy to:
    - read "scores_all.csv" file
    - delete the first row (with column headings)
    - fill out the missing data with 0s
    - print the resulting data array and save it to the file "scores.npy"
'''

import numpy as np
from numpy import genfromtxt


def main():

    scores_all = genfromtxt("Scores_all.csv", delimiter=",")
    scores = scores_all[1:]
    scores[np.isnan(scores)] = 0
    scores_int = scores.astype(int)
    print(scores_int)
    np.save("scores", scores_int)
    

main()