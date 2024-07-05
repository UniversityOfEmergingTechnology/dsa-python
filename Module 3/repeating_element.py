# def firstRepeatingBrute(arr) : 
#     for i in range(len(arr)) :
#         for j in range(i + 1 , len(arr)):
#             if arr[i] == arr[j] :
#                 return arr[i]
    
#     return -1
import sys

def firstRepeatingHash(arr):
    counts = {}

    for i in range(len(arr)) :
        if arr[i] in counts :
            counts[arr[i]][0] += 1
        else :
            # we are hashing counts , index
            counts[arr[i]] = [1 , i]
    minvalue = sys.maxsize

    for entry in counts.items():
        if entry[1][0] > 1 :
            if minvalue > entry[1][1] : 
                minvalue =  entry[1][1]

    return minvalue + 1
arr = [4 , 2 , 5 ,2 ,3 , 5]
result = firstRepeatingHash(arr)

print(result)