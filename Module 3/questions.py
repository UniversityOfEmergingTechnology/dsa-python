# find unique element

# def findUnique(arr):
#     num_bool = {} 
#     for i in range(len(arr)) :
#         if arr[i] not in num_bool :
#             num_bool[arr[i]] = False


#         for j in range(i + 1 , len(arr)) :
#             if num_bool[arr[i]] == True:
#                 break
#             if(arr[i] == arr[j]) :
#                 num_bool[arr[i]] = True
#                 break
                

#     for keys , values in num_bool.items() :
#         print(f"{keys} : {values}")    

# def findUnique(arr) :
#     unique = 0

#     for num in arr :
#         unique = unique ^ num
    
#     return unique

# arr = [2,3,3,2,4,5,5]


# result = findUnique(arr)

# print(result)


# findUnique(arr)



# second question unique elements in 2 arrays

# def uniqueElements(arr1 , arr2) :
#     set1 = set(arr1)
#     set2 = set(arr2)
#     return (set1 - set2).union(set2 - set1)

# arr1 = [1,2,3]
# arr2 = [3,4,5]
# arr3 = uniqueElements(arr1 , arr2)
# print(arr3)

# T.C - O(n + m)
# S.C = O(n + m)


# problem - 3 intersection of 2 arrays

# def intersection(arr1 , arr2) :
#     return list(set(arr1) & set(arr2))


# arr1 = [1,2,3,3 , 4]
# arr2 = [1,2,3]

# print(3 & 3)

# print(intersection(arr1 , arr2))

# T.C = O(n + m)
# S.C = O(min(n,m))