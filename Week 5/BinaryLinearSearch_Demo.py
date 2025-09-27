# Generate random numbers based on user intent
# Ask user for 3 numbers to search
# Perform Linear & Binary Search for each number

import random
import time
from typing import List

# Linear Search Function

def linear_search(arr: List[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search Function

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Main Application for Searching

def search_app():
    n = int(input("How many random numbers to generate? "))
    low = int(input("Enter the minimum value: "))
    high = int(input("Enter the maximum value: "))
    
    numbers = [random.randint(low, high) for _ in range(n)]
    numbers.sort()
    print("\nGenerated numbers (sorted):")
    print(numbers)
    
    queries = []
    for i in range(3):
        q = int(input(f"Enter Search Number {i+1}: "))
        queries.append(q)
        
    for q in queries:
        print(f"\nSearching for {q}...")
        
        
        # Linear Search
        start = time.perf_counter()
        idx_linear = linear_search(numbers, q)
        end = time.perf_counter()
        
        if idx_linear != -1:
            print(f"[Linear] Found at index {idx_linear} in {end - start:.6f} sec -> You are Lucky!")
        else:
            print(f"[Linear] Sorry, try again, number {q} not found.")
        
        # Binary Search
        start = time.perf_counter()
        idx_binary = binary_search(numbers, q)
        end = time.perf_counter()
        
        if idx_binary != -1:
            print(f"[Binary] Found at index {idx_binary} in {end - start:.6f} sec -> You are Lucky!")
        else:
            print(f"[Binary] Sorry, try again, number {q} not found.")
        
    print("\nSearch Demo completed!")
    
# Run the App
if __name__ == "__main__":
    search_app()