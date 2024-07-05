def integerSquareRoot(X):
    start , end = 1 , X
    ans = 0
    while start <= end:
        mid = start + (end - start) // 2

        if mid * mid <= X:
            ans = mid
            start = mid + 1
        else :
            end = mid - 1
    
    return ans


def squareRoot(X , precision = 0.0001):
    integer_part = integerSquareRoot(X)
    step_size = 0.1

    while step_size >= precision :
        while integer_part * integer_part <= X:
            integer_part += step_size
        integer_part -= step_size
        step_size /= 10
    
    return round(integer_part , 4)


print(squareRoot(10))


