def fib_recursive(n):
    # base case
    if n <= 1:
        return n
    
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memoization(n , memo = {}):
    # base case
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = fib_memoization(n - 1 , memo) + fib_memoization(n - 2 , memo)

    return memo[n]


def fib_bottom_up(n):
    # base case
    if n <= 1:
        return n
    
    fib = [0 , 1]

    for i in range(2 , n + 1):
        sum = fib[i - 1] + fib[i - 2]
        fib.append(sum)


    return fib[n]

def fib_tabulation(n):

    if n <= 1:
        return n
    
    prev2 = 0
    prev1 = 1
    
    for i in range(2 , n + 1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current
    
    return current



print(fib_recursive(10))
print(fib_memoization(50))
print(fib_bottom_up(50))
print(fib_tabulation(50))


