def maxSegments(n , x , y ,z):
    # base case
    if n == 0 :
        return 0
    
    # invalid case
    if n < 0 :
        return -1
    
    # recursive case - try each cut and take maximum
    res = max(maxSegments(n - x , x ,y , z) , 
              maxSegments(n - y , x , y ,z) ,
              maxSegments(n - z , x , y , z))

    # if none of cuts lead to a valid solution return -1
    if res == -1 :
        return -1
    
    # return maximum count of segments + 1 for current cut
    return res + 1

print(maxSegments(7 , 5 , 2 , 2))
