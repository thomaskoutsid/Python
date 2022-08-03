'''
Thomas Koutsidis
July 1st, 2022

Question 2

This program uses NumPy to read file "scores.npy" and create a NumPy array "score_headings" with the following columns:
    id numbers
    weighted scores for hw
    weighted scores for labs
    weighted scores for final projevys
    weighted scores for midterm 1
    weighted scores for quizzes
    weighted scores for midterm 2
It prints "score_headings" and stores it to file "score_heading.npy"
'''

import numpy as np


def main():
     scores = np.load("scores.npy")
     np.set_printoptions(suppress=True)

     identity = np.array(scores[1:, 0])
     
     homework = np.array(((scores[1:, 1:7].sum(axis = 1)) / 600) * 20)
     homework = np.around(homework, decimals = 1)
     
     lab = np.array(((scores[1:, 7:18].sum(axis = 1)) / 1100) * 30)
     lab = np.around(lab, decimals = 1)
     
     final = np.array(((scores[1:, 18]) / 100) * 10)
     final = np.around(final, decimals = 1)
     
     midterm1 = np.array(((scores[1:, 19]) / 100) * 10)
     midterm1 = np.around(midterm1, decimals = 1)
     
     quizzes = np.array(((scores[1:, 20:29].sum(axis = 1)) / 90) * 15)
     quizzes = np.around(quizzes, decimals = 1)
     
     midterm2 = np.array(((scores[1:, 29]) / 100) * 15)
     midterm2 = np.around(midterm2, decimals = 1)
   
     headings = np.array([identity, homework, lab, final, midterm1, quizzes, midterm2])
     score_headings = np.transpose(headings)
     
    
     print(score_headings)
     np.save("score_headings", score_headings)
     
    
main()
     
     
    
