arr = [-1 , -6 , 3 , 5 , -10 , 7 , -11 ]

left = 0
right = len(arr) - 1

while left < right :
    if arr[left] <  0:
        left += 1
    if arr[right] > 0:
        right -= 1
    
    if arr[left] > 0 and arr[right] < 0:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1

print(arr) 
# T.C = O(N)
# S.C = O(1)