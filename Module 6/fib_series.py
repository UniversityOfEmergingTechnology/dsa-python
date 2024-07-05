def fib_number_iterative(n):
    first_number, second_number = 0 , 1

    for _ in range(n):
        first_number , second_number = second_number , first_number + second_number

    return first_number

def fib_number(n):

    # base case
    # 1st number = 0 and 2nd number = 1
    if n == 2 :
        return 1
    if n == 1 :
        return 0
    
    # for any other number we will call recursive step
    return fib_number(n - 1) + fib_number(n - 2)

print(fib_number_iterative(5))