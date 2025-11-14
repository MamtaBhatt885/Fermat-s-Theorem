# Fermat-s-Theorem

Programmers: Mamta Bhatt and Megan Powers

Email: mbhatt@lewisu.edu and meganlpowers@lewis.edu

Course: CPSC 60500 Section 4,

Professor: Dr. Fadi Wedyan Software Engineering, Assignment 1

Program language: Python 

File Name: fermat_near_miss.py

Program Description: Mathematician Pierre Fermat's Last Theorem states that there are no natural numbers such that x^n + y^n = x^n, but this equation can get close to being true. This program discovers values for x, y, and z given a value of n which make the equation close to being true. These sets of values are called Near Misses. To run this program, a user first enters a chosen value of n, a natural number between 3 and 11. Then the user enters a chosen value of k, a natural number between 11 and 50 which tells the program which values of x, y, and z to test the equation with. The program finds the Near Miss value of each equation using values of x, y, and y each between 11 and the user inputted k. A "miss" value shows the user the actual natural number difference between the two sides of the equation. A "relative miss" value shows the user the relative closeness of the equation being true by dividing the "miss" by x^n = y^n. The "relative miss" is also shown as a percentage.
As the program runs the equations, the smallest "relative miss" is considered the best Near Miss and is shown to the user. When all equations have been run, the user is given values for the best Near Miss

