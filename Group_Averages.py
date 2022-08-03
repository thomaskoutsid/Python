'''
Thomas Koutsidis
July 2nd, 2022

Question 5

This program uses NumPy to calculate and print average of each assignment group.
'''

import numpy as np


def main(): 
    print("Program to calculate assignment group averages.")
    print("\t")
    scores = np.load("scores.npy")
    np.set_printoptions(suppress=True)

    homework0 = np.array(scores[:,1].sum(axis = 0))   
    homework1 = np.array(scores[:,2].sum(axis = 0))    
    homework2 = np.array(scores[:,3].sum(axis = 0))
    homework3 = np.array(scores[:,4].sum(axis = 0))
    homework4 = np.array(scores[:,5].sum(axis = 0))
    homework5 = np.array(scores[:,6].sum(axis = 0))
    total_hw = homework0 + homework1 + homework2 + homework3 + homework4 + homework5    
    hw_count = len(scores[:,1]) + len(scores[:,2]) + len(scores[:,3]) + len(scores[:,4]) + len(scores[:,5]) + len(scores[:,6])
    hw_avg = total_hw / hw_count
    hw_avg = np.around(hw_avg, decimals = 1)
    print("Homework average:", hw_avg)
    
    lab1 = np.array(scores[:,7].sum(axis = 0))
    lab2 = np.array(scores[:,8].sum(axis = 0))
    lab3 = np.array(scores[:,9].sum(axis = 0))
    lab4 = np.array(scores[:,10].sum(axis = 0))
    lab5 = np.array(scores[:,11].sum(axis = 0)) 
    lab6 = np.array(scores[:,12].sum(axis = 0))
    lab7 = np.array(scores[:,13].sum(axis = 0))
    lab8 = np.array(scores[:,14].sum(axis = 0))
    lab9 = np.array(scores[:,15].sum(axis = 0))
    lab10 = np.array(scores[:,16].sum(axis = 0))
    lab11 = np.array(scores[:,17].sum(axis = 0))
    total_lab = lab1 + lab2 + lab3 + lab4 + lab5 + lab6 + lab7 + lab8 + lab9 + lab10 + lab11
    lab_count = len(scores[:,7]) + len(scores[:,8]) + len(scores[:,9]) + len(scores[:,10]) + len(scores[:,11]) + len(scores[:,12]) + len(scores[:,13]) + len(scores[:,14]) + len(scores[:,15]) + len(scores[:,16]) + len(scores[:,17])
    lab_avg = total_lab / lab_count
    lab_avg = np.around(lab_avg, decimals = 1)
    print("Lab average:", lab_avg)
    
    quiz1 = np.array(scores[:,20].sum(axis = 0))
    quiz2 = np.array(scores[:,21].sum(axis = 0))
    quiz3 = np.array(scores[:,22].sum(axis = 0))
    quiz5 = np.array(scores[:,23].sum(axis = 0))
    quiz6 = np.array(scores[:,24].sum(axis = 0))
    quiz7 = np.array(scores[:,25].sum(axis = 0))
    quiz8 = np.array(scores[:,26].sum(axis = 0))
    quiz9 = np.array(scores[:,27].sum(axis = 0))
    quiz10 = np.array(scores[:,28].sum(axis = 0))
    total_quiz = quiz1 + quiz2 + quiz3 + quiz5 + quiz6 + quiz7 + quiz8 + quiz9 + quiz10
    quiz_count = len(scores[:,20]) + len(scores[:,21]) + len(scores[:,22]) + len(scores[:,23]) + len(scores[:,24]) + len(scores[:,25]) + len(scores[:,26]) + len(scores[:,27]) + len(scores[:,28])
    quiz_avg = total_quiz / quiz_count
    quiz_avg = np.around(quiz_avg, decimals = 1)
    print("Quiz average:", quiz_avg)
    
    final1 = np.array(scores[:,18].sum(axis = 0)) / len(scores[:,18])
    final1 = np.around(final1, decimals = 1)
    print("Project average:", final1)
    
    mid1 = np.array(scores[:,19].sum(axis = 0)) / len(scores[:,19])
    mid1 = np.around(mid1, decimals = 1)
    print("Midterm 1 average:", mid1)
    
    mid2 = np.array(scores[:,29].sum(axis = 0)) / len(scores[:,29])
    mid2 = np.around(mid2, decimals = 1)
    print("Midterm 2 average:", mid2)
    
    
main()
