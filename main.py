# -------------------------------------------------------------
# Program Title: Fermat's Last Theorem Near Miss Finder
# File Name: fermat_near_miss.py
# Programmers: Mamta Bhatt and Megan Powers
# Emails: mbhatt@lewisu.edu, meganlpowers@lewis.edu
# Course: CPSC 60000 Section 4- Software Engineering
# Date Submitted: November 16, 2025
# Description: Searches for near-miss integer combinations for Fermat’s Last Theorem.
# [....should this include a shortened version of the READ ME program description?....]
# Language: Python, created on PyCharm version 2021.3.2
# External Files: None
# Files Created: none
# Libraries Used: None
# How to Run: [...........] See README for more instructions.
# Resources Used: [...........]
# -------------------------------------------------------------


# Prompt user for n (integer), prompt again if invalid
n = int(input("Please enter a whole number value for n: "))
# 	Check that n is greater than 2
while n < 3:
    n = int(input("Please enter a whole number value of n that is no less than 3: "))
# 	Check that n is less than 12
while n > 12:
    n = int(input("Please enter a whole number value of n that is no greater than 12: "))
# TEST PRINT (delete later):
print("n = ", n)



# Prompt user for k (integer), prompt again if invalid
k = int(input("Please enter a whole number value for k: "))
# 	Check that k is greater than 10
while k < 10:
    k = int(input("Please enter a whole number value of k that is no less than 11: "))
# 	Check that k is less than ???? (a large number to avoid crashes)
while k > 20:
    k = int(input("Please enter a whole number value of n that is no greater than 20: "))
# TEST PRINT (delete later):
print("k = ", k)



# Create the next set of values to test
# 	Start with x=y=z=10
x = int(10)
y = int(10)
z = int(10)
# TEST PRINT (delete later):
print("x = ", x, "y = ", y, "z = ", z)
# Increase x by 1 until x=k, repeat loop:
## while x <= k:
##    **run the calculations**
##    x += 1
# Then increase y by 1 until y=k, repeat loop:
## while y <= k:
##    **run the calculations**
##    y += 1
# Then increase z by 1 until z^n > (x^n + y^n)
## while z**n > (x**n + y**n):
##    **run the calculations**
##    z += 1



# Find the amount of the actual miss (positive integer "a") for z and z+1, and return the smaller value
# Compare [(x^n + y^n) - z^n] and [(z+1)^n - (x^n + y^n)], then assign the smaller value to "a" (ignore negativity)
if abs(((x**n + y**n) - z**n)) < ((z+1)**n - (x**n + y**n)):
    a = int(abs((x ** n + y ** n) - z ** n))
if abs(((x**n + y**n) - z**n) > ((z+1)**n - (x**n + y**n))):
    a = int(abs((z+1)**n - (x**n + y**n)))
# TEST PRINT (delete later):
print("x^n + y^n = ", x**n+y**n, ", z^n = ", z**n, ", (z+1)^n = ", (z+1)**n)
# TEST PRINT (delete later):
print("The actual miss, a = ", a)



# Find the amount of the relative misses (float "r"), which is the actual miss divided by x^n + y^n
r = float(a / ((x**n) + (y**n)))
# TEST PRINT (delete later):
print("The relative miss, r = ", r)



# Compare the newest relative miss with the previously smallest relative miss
# 	If the newest relative miss is greater, then continue
# 	If the newest relative miss is smaller, then replace the old relative miss and print




# Print the latest best result
# 	Print and label current x, y, z values (integers)
print("When x=", x, ", y= ", y, ", and z=", z)
# 	Print and label the actual miss (integer)
print("then the actual miss is ", a)
# 	Print and label the relative miss (as a percentage)
print("and the relative miss is ", r*100, "%")



# Print and label best result
# Create a pause at the end or ask the user to type after reading to continue