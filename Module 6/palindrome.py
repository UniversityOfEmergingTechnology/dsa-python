def isPalindrome(s , start = 0 , end = None) :
    if end is None :
        end = len(s) - 1
    
    # base case if string is empty or a single character
    if start >= end :
        return True
    
    # check if first and last char match
    if s[start] != s[end] :
        return False
    

    # recursive step
    return isPalindrome(s , start + 1 , end - 1)

print(isPalindrome("racecar"))
print(isPalindrome("hello"))