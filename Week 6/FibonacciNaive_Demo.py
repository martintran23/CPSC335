# Fibonacci Numbers with Naive Recursion

def fib_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(6))

# Fibonacci with Memoization (Top Down DP approach)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib_memo(n-1) + fib_memo(n-2)

print(fib_memo(6))
print(fib_memo(10))

# Fibonacci with Tabulation
def fib_tab(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i+2]
    return dp[n]

print(fib_memo(6))
print(fib_memo(10))