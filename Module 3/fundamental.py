# # count zeroes and ones in array

# def count_zeroes_and_ones(arr) :
#     count_zero , count_one = 0 , 0
#     for num in arr : 
#         if num == 0 : 
#             count_zero += 1
#         else :
#             count_one += 1
#     return count_zero , count_one

# arr = [0 ,1 , 0 ,0 ,1 ,0,1]

# count_zero , count_one = count_zeroes_and_ones(arr)

# print(f"Zeroes : {count_zero} , Ones : {count_one}")


# # Time complexity  = O(N)
# # Space complexity = O(1)


# Finding the maximum number in an array

# def find_max(arr) :
#     max_num = arr[0]
#     for num in arr :
#         if num > max_num :
#             max_num = num
    
#     return max_num

# arr = [3,5,9,1]

# print("Maximum number : " , find_max(arr))

# # time complexity : O(N)
# # space complexity  : O(1)

# Extreme print in array
# def find_extreme(arr) : 
#     min_val , max_val = arr[0] , arr[0]

#     for num in arr:
#         if num < min_val :
#             min_val = num
#         elif num > max_val : 
#             max_val = num
#     return min_val , max_val

# arr = [2,8,5,3]

# print(f"Min : {find_extreme(arr)[0]} , Max : {find_extreme(arr)[1]}")

# Time complexity : O(n)
# space complexity : O(1)

# reversing an array

def reverse_array(arr):
    return arr[::-1] # slicing from end to start

arr = [1,2,3,4,5]
print("Reversed array " , reverse_array(arr))
