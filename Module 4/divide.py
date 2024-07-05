def divide(dividend , divisor):
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    divisor , dividend = abs(divisor) , abs(dividend)

    start , end = 0 , dividend
    ans = 0
    while start <= end: 
        middle = start + (end - start) // 2

        if middle * divisor <= dividend :
            ans = middle
            start = middle + 1
        else :
            end = middle - 1

    return sign * ans

print(divide(-10 , -3))

