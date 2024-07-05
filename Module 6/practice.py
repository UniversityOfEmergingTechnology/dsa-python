# def print_list_recursively(lst , index = 0) :
#     # base case
#     if index == len(lst):
#         return

#     print(lst[index])
#     print_list_recursively(lst , index + 1)


# nums = [1,2,3,4,5]
# print_list_recursively(nums)


# finding maximum and minimum in a list recursively

# def find_max_recursively(lst , index = 0):
#     # base case
#     if index == len(lst) - 1:
#         return lst[index]
    
#     # recursively find the max in rest of the list
#     max_of_rest = find_max_recursively(lst , index + 1)

#     return max(lst[index] , max_of_rest)

# nums = [1,5,3,9,2]
# print(find_max_recursively(nums))


# find minimum number in a list

# T.c - O(n)


# printing all digits of a number recursively

def print_digits_recursively(number):
    if number == 0:
        return
    print_digits_recursively(number // 10)
    
    print(number % 10)

print_digits_recursively(97432)