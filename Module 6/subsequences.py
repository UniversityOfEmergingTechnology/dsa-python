def generateSubsequences(s , index = 0 , curr = ""):
    # base case if we have reached the end of the string
    if index == len(s):
        print(curr)
        return
    
    # include the character
    print("Including call for index : " , index , " curr string : " , curr)
    generateSubsequences(s , index + 1 , curr + s[index])

    # exclude the character
    print("Excluding call for index : " , index , " curr string : " , curr)
    generateSubsequences(s , index + 1 , curr)

generateSubsequences("abc")