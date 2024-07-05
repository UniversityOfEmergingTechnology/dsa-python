def printAllSubarrays(arr , start = 0 , curr = []) : 
    # base case 
    if start == len(arr) :
        print(curr)
        return
    
    # include the current element
    curr.append(arr[start])
    printAllSubarrays(arr , start + 1 , curr)
    # exclude the current element (backtrack and remove the last added element)
    curr.pop()
    printAllSubarrays(arr , start + 1 , curr)


arr = [ 1,2,3]
printAllSubarrays(arr)

