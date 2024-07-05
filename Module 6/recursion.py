# learning recursion

# print 1 to 5

# how we used to print earlier


# iteration method
# for i in range(0 , 5):
#     print(i + 1)


# recursion method

# tail recursion
# def print_recursion(curr_number , total_numbers) :

#     # base case
#     if(curr_number > total_numbers):
#         return

#     print(curr_number , end = ' ')
#     # recursive step
#     print_recursion(curr_number + 1 , total_numbers)

# head recursion

def print_recursion(curr_number , total_numbers) :

    # base case
    if(curr_number > total_numbers):
        return
    # recursive step
    print_recursion(curr_number + 1 , total_numbers)

    print(curr_number , end = ' ')

print_recursion(1 , 5)