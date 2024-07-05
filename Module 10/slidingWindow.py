from collections import deque

def findFirstNegative(arr , k):
    n = len(arr)

    # queue to hold indices of negative numbers
    neg_indices = deque()

    result = []

    # fill the queue with inital negative indices

    for i in range(k):
        if arr[i] < 0 :
            neg_indices.append(i)

    print(f"Neg indices" , neg_indices)
    

    # process the rest of the array
    for i in range( k , n):
        # print(f" i is " , i)
        # append the first negative from the queue or 0 if queue if empty
        result.append(arr[neg_indices[0]] if neg_indices else 0) 
        # print(f"Updated result " , result)
        # remove indices that are out of the current window
        while neg_indices and neg_indices[0] <= i - k :
            neg_indices.popleft()
        # print(f"Updated queue " , neg_indices)
        # add new negative new indices
        if arr[i] < 0:
            neg_indices.append(i)
        # print(f"Appending in  queue " , neg_indices)
        
    # append the first negative for the last window
    result.append(arr[neg_indices[0]] if neg_indices else 0)   

    return result 

arr = [-2,3,-1,5,-4, 2 , -6]
k=3
print(findFirstNegative(arr , k))