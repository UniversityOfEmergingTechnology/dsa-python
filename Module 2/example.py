# def linear_Search(elements , target) :
#     for i in range(len(elements)) :
#         if(elements[i] == target) :
#             print("Element found")
#             return
#     print("Element not found")





# elements = [1,2,3,4,5]
# target = 5
# linear_Search(elements , target)


# example 1 space complexity constant space O(1)

# def find_max(arr):
#     max_val = arr[0]

#     for num in arr :
#         if num > max_val :
#             max_val = num

#     return max_val


# example 2 linear space O(n)

# def duplicate_list(arr)
#     new_arr = arr
#     return new_arr



# sum of elements in a list

def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

# T.C - O(n)
# S.C - O(1)

# checking for duplicates in a list

def has_duplicates(lst):
    seen = set()

    for element in lst:
        if element in seen:
            return True
        else :
            seen.add(element)
    return False



# T.C - O(n)
# S.C - O(n)


# nested loops for pair sums

def find_pair_sums(arr):
    pairs = []

    for i in range(len(arr)) :
        for j in range(i + 1 , len(arr)) :
            pairs.append(arr[i] + arr[j])  
    return pairs

# TC - O(n^2)
# SC - O(n^2)

# using dictionary to count frequencies

def count_frequencies(lst):
    frequency = {}

    for item in lst :
        if item in frequency :
            frequency[item] += 1
        else :
            frequency[item] = 1
    return frequency
# T.C - O(n)
# S.C - O(n)

# fibonacci using iteration
def fibonacci(n):
    if n <= 1 :
        return n
    
    a , b =  0 , 1

    for i in range(2 , n + 1):
        a , b =  b , a + b


# T.C - O(n)
# S.C - O(1)
        
# reversing a string
def reverse_string(s):
    return s[::-1]

# T.C - O(n)
# S.C - O(n)