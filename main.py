# OPENING COMMENT:
# Program Name: Looking for Fermat's Last Theorem Near Misses
# •	the name of the file that holds your program
# •	a list of any external files necessary to run your program
# •	a list of external files your program creates. If you list any external files, briefly explain what each of them contains
# Programmers: Mamta Bhatt and Megan Powers
# ??????? and meganlpowers@lewisu.edu
# CPSC 60500 Section 4
# Submission Date: November 16, 2025
# This program helps an interactive user search for near misses of Fermat's Last Theorem. While x^n + y^n = z^n cannot be true, we will find values that come close to it being true. x, y, z, and n are all positive integers, and n is greater than two and less than 12. The user will input n and also k which will limit the number of attempts.
# •	any resources you used to complete the program (Always give credit where credit is due; for example, if you used a website to check on an algorithm, list that here.)



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