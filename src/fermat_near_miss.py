# -------------------------------------------------------------
# Program Title: Fermat's Last Theorem Near Miss Finder
# File Name: fermat_near_miss.py
# Programmers: Mamta Bhatt and Megan Powers
# Emails: mbhatt@lewisu.edu, meganlpowers@lewis.edu
# Course: CPSC 60500 Section 4- Software Engineering
# Date Submitted: November 16, 2025
# Description: Searches for values that create a near-miss for Fermat’s Last Theorem. Fermat's Last Theorem states that
# there are no natural numbers such that x^n + y^n = x^n, but this equation can get close to being true. This program
# discovers values for x, y, and z given a value of n which make the equation close to being true. These sets of values
# are called Near Misses. To run this program, a user first enters a chosen value of n, a natural number between 3 and
# 11. Then the user enters a chosen value of k, a natural number between 11 and 50 which tells the program which values
# of x, y, and z to test the equation with. The program finds the Near Miss value of each equation using values of x, y,
# and y each between 11 and the user inputted k. A "miss" value shows the user the actual natural number difference
# between the two sides of the equation. A "relative miss" value shows the user the relative closeness of the equation
# being true by dividing the "miss" by x^n = y^n. The "relative miss" is also shown as a percentage. As the program runs
# the equations, the smallest "relative miss" is considered the best Near Miss and is shown to the user. When all
# equations have been run, the user is given values for the best Near Miss.
# Language: Python 3.11, created on PyCharm version 2021.3.2
# External Files: None
# Files Created: none
# Libraries Used: None
# How to Run: python, pyinstaller. Run fermat_near_miss.exe
# Resources Used: Google, YouTube and ChatGPT to learn GitHub
# -------------------------------------------------------------


# ASK THE USER FOR INPUT

# The exponent, n:
n = int(input("Enter a natural number value for n: "))
# Check that n is greater than 2
while n < 3:
    n = int(input("Enter a natural number value of n that is no less than 3: "))
# Check that n is less than 12
while n > 11:
    n = int(input("Enter a natural number value of n that is no greater than 11: "))

# The upper limit, k:
k = int(input("Enter a natural number value for k: "))
#  Check that k is greater than 10
while k < 11:
    k = int(input("Enter a natural number value of k that is no less than 11: "))
#  Check that k is less than 500
while k > 500:
    k = int(input("Enter a natural number value of k that is no greater than 500: "))

# Initialize before the loops
smallest_relative_miss = 1.0  # large number to start
best_x, best_y, best_z = 0, 0, 0
best_miss = 0

# Start looping through all x, y combinations
for x in range(10, k + 1):
    for y in range(10, k + 1):
        sum_val = x ** n + y ** n
        z = int(sum_val ** (1 / n))
        miss_1 = abs(sum_val - z ** n)
        miss_2 = abs((z + 1) ** n - sum_val)
        miss = min(miss_1, miss_2)
        relative_miss = miss / sum_val

        # Check if this is the smallest miss so far
        if relative_miss < smallest_relative_miss:
            smallest_relative_miss = relative_miss
            best_x, best_y, best_z = x, y, z
            best_miss = miss
            print(f"New smallest near miss: x={x}, y={y}, z={z}, miss={miss}, relative miss={relative_miss:.8f}")

# Print final result
print("\n--- Final Smallest Near Miss ---")
print(f"x = {best_x}, y = {best_y}, z = {best_z}")
print(f"Miss = {best_miss}")
print(f"Relative miss = {smallest_relative_miss:.8f}")


input("\nPress Enter to exit...")
