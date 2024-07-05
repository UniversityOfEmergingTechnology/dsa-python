def reverseString(s):
    # base case 
    if len(s) <= 1 :
        return s
    

    # recursive step - reverse the substring and append the first character to its end
    return reverseString(s[1:]) + s[0]

s = "hello"

print(reverseString(s))