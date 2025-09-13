# Python program to find the MinValue in the given List

# Step 1
numbers = input("Enter a list of numbers separated by spaces: ")

# Step 2
L = [int(x) for x in numbers.split()]

# Step 3
minValue = L[0] # Assuming the first num as a Min value

# Step 4
for n in L[1:]:
    # Step 5
    if n < minValue:
        minValue = n
        
# Step 6
print("The minimum value in the list is:", minValue)