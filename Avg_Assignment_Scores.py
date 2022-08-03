'''
Thomas Koutsidis
July 2nd, 2022

Question 4

This program uses NumPy to calculate and print the average score for each assignment.
'''

import numpy as np


def main():
    scores = np.load("scores.npy")
    np.set_printoptions(suppress=True)

    homework0 = np.array(scores[:,1].sum(axis = 0)) / len(scores[:,1])
    homework0 = np.around(homework0, decimals = 1)
    print("Homework 0 average:", homework0)
    
    homework1 = np.array(scores[:,2].sum(axis = 0)) / len(scores[:,2])    
    homework1 = np.around(homework1, decimals = 1)
    print("Homework 1 average:", homework1)
    
    homework2 = np.array(scores[:,3].sum(axis = 0)) / len(scores[:,3])
    homework2 = np.around(homework2, decimals = 1)
    print("Homework 2 average:", homework2)
    
    homework3 = np.array(scores[:,4].sum(axis = 0)) / len(scores[:,4])
    homework3 = np.around(homework3, decimals = 1)
    print("Homework 3 average:", homework3)
    
    homework4 = np.array(scores[:,5].sum(axis = 0)) / len(scores[:,5])
    homework4 = np.around(homework4, decimals = 1)
    print("Homework 4 average:", homework4)
    
    homework5 = np.array(scores[:,6].sum(axis = 0)) / len(scores[:,6])
    homework5 = np.around(homework5, decimals = 1)
    print("Homework 5 average:", homework5)
    
    print("\t")
    
    lab1 = np.array(scores[:,7].sum(axis = 0)) / len(scores[:,7])
    lab1 = np.around(lab1, decimals = 1)
    print("Lab 1 average:", lab1)
    
    lab2 = np.array(scores[:,8].sum(axis = 0)) / len(scores[:,8])
    lab2 = np.around(lab2, decimals = 1)
    print("Lab 2 average:", lab2)
    
    lab3 = np.array(scores[:,9].sum(axis = 0)) / len(scores[:,9])
    lab3 = np.around(lab3, decimals = 1)
    print("Lab 3 average:", lab3)
    
    lab4 = np.array(scores[:,10].sum(axis = 0)) / len(scores[:,10])
    lab4 = np.around(lab4, decimals = 1)
    print("Lab 4 average:", lab4)
    
    lab5 = np.array(scores[:,11].sum(axis = 0)) / len(scores[:,11])
    lab5 = np.around(lab5, decimals = 1)
    print("Lab 5 average:", lab5)
    
    lab6 = np.array(scores[:,12].sum(axis = 0)) / len(scores[:,12])
    lab6 = np.around(lab1, decimals = 1)
    print("Lab 6 average:", lab6)
    
    lab7 = np.array(scores[:,13].sum(axis = 0)) / len(scores[:,13])
    lab7 = np.around(lab7, decimals = 1)
    print("Lab 7 average:", lab7)
    
    lab8 = np.array(scores[:,14].sum(axis = 0)) / len(scores[:,14])
    lab8 = np.around(lab8, decimals = 1)
    print("Lab 8 average:", lab8)
    
    lab9 = np.array(scores[:,15].sum(axis = 0)) / len(scores[:,15])
    lab9 = np.around(lab9, decimals = 1)
    print("Lab 9 average:", lab9)
    
    lab10 = np.array(scores[:,16].sum(axis = 0)) / len(scores[:,16])
    lab10 = np.around(lab10, decimals = 1)
    print("Lab 10 average:", lab10)
    
    lab11 = np.array(scores[:,17].sum(axis = 0)) / len(scores[:,17])
    lab11 = np.around(lab11, decimals = 1)
    print("Lab 11 average:", lab11)
    
    print("\t")
    
    quiz1 = np.array(scores[:,20].sum(axis = 0)) / len(scores[:,20])
    quiz1 = np.around(quiz1, decimals = 1)
    print("Quiz 1 average:", quiz1)
    
    quiz2 = np.array(scores[:,21].sum(axis = 0)) / len(scores[:,21])
    quiz2 = np.around(quiz2, decimals = 1)
    print("Quiz 2 average:", quiz2)
    
    quiz3 = np.array(scores[:,22].sum(axis = 0)) / len(scores[:,22])
    quiz3 = np.around(quiz3, decimals = 1)
    print("Quiz 3 average:", quiz3)
    
    quiz5 = np.array(scores[:,23].sum(axis = 0)) / len(scores[:,23])
    quiz5 = np.around(quiz5, decimals = 1)
    print("Quiz 5 average:", quiz5)
    
    quiz6 = np.array(scores[:,24].sum(axis = 0)) / len(scores[:,24])
    quiz6 = np.around(quiz6, decimals = 1)
    print("Quiz 6 average:", quiz6)
    
    quiz7 = np.array(scores[:,25].sum(axis = 0)) / len(scores[:,25])
    quiz7 = np.around(quiz7, decimals = 1)
    print("Quiz 7 average:", quiz7)
    
    quiz8 = np.array(scores[:,26].sum(axis = 0)) / len(scores[:,26])
    quiz8 = np.around(quiz8, decimals = 1)
    print("Quiz 8 average:", quiz8)
    
    quiz9 = np.array(scores[:,27].sum(axis = 0)) / len(scores[:,27])
    quiz9 = np.around(quiz9, decimals = 1)
    print("Quiz 9 average:", quiz9)
    
    quiz10 = np.array(scores[:,28].sum(axis = 0)) / len(scores[:,28])
    quiz10 = np.around(quiz10, decimals = 1)
    print("Quiz 10 average:", quiz10)
    
    print("\t")
    
    final1 = np.array(scores[:,18].sum(axis = 0)) / len(scores[:,18])
    final1 = np.around(final1, decimals = 1)
    print("Final project average:", final1)
    
    mid1 = np.array(scores[:,19].sum(axis = 0)) / len(scores[:,19])
    mid1 = np.around(mid1, decimals = 1)
    print("Midterm 1 average:", mid1)
    
    mid2 = np.array(scores[:,29].sum(axis = 0)) / len(scores[:,29])
    mid2 = np.around(mid2, decimals = 1)
    print("Midterm 2 average:", mid2)
    
    
main()
