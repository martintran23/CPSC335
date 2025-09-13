# Python program to find the MaxValue in the given List

# Step 1
numbers = input("Enter a list of numbers separated by spaces: ")

# Step 2
L = [int(x) for x in numbers.split()]

# Step 3
maxValue = L[0] # Assuming the first num as a Max value

# Step 4
for n in L[1:]:
    # Step 5
    if n > maxValue:
        maxValue = n
        
# Step 6
print("The maximum value in the list is:", maxValue)