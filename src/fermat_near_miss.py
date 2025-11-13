# -------------------------------------------------------------
# Program Title: Fermat's Last Theorem Near Miss Finder
# File Name: fermat_near_miss.py
# Programmers: Mamta Bhatt and Megan Powers
# Emails: mbhatt@lewisu.edu, [partner_email]
# Course: CPSC 60000 - Software Engineering
# Date Submitted: [Date]
# Description: Searches for near-miss integer combinations for Fermat’s Last Theorem.
# External Files: None
# Libraries Used: None
# -------------------------------------------------------------


#Ask user for the input

# the exponent
n =  int(input("Enter a number between 3 and 11: "))

# the upper limit
k = int(input("Enter the upper limit for x and y that should be greater than 10: "))

if n < 3 or n>=12 and k<10:
    print("Invalid input. Please enter n between 3 and 11 and k greater than 10")
    exit()

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