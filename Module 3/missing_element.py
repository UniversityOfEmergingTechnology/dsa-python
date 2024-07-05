# def findMissingBrute(arr, extreme_limit) :
#     max_val = max(arr)
#     missing = []

#     for i in range(1 , extreme_limit + 1) :
#         if i not in arr:
#             missing.append(i)
    
#     return missing

# def findMissingNegativeMarking(arr):
#     for num in arr:
#         index = abs(num) - 1 
#         if arr[index] > 0:
#             arr[index] = -arr[index]
#     return [i + 1 for i in range(len(arr)) if arr[i] > 0]

def findMissingHash(arr) :
    num_set = set(arr)
    max_val = max(arr)

    missing = [num for num in range(1 , max_val + 1) if num not in num_set]
    return missing


arr = [1,2,2,3,5]

# result = findMissingBrute(arr , 12)
# result= findMissingNegativeMarking(arr)
result = findMissingHash(arr)
print(result)

# T.C - O(n x m)