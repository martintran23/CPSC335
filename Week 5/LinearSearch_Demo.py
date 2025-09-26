import time
from typing import List, Any

def linear_search(arr: List[Any], target: Any) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def timed_linear_search(arr: List[Any], target: Any) -> int:
    start = time.perf_counter()
    result = linear_search(arr, target)
    end = time.perf_counter()
    print(f"[Linear] search n={len(arr)} in {end - start:.6f} sec; result index ={result}")
    
# Demo
numbers = [23, 45, 12, 89, 34, 67]
print("Search 89:", timed_linear_search(numbers, 89))
print("Search 50:", timed_linear_search(numbers, 50))