def permuteString(s) :
    
    def backtrack(i = 0):
        # if we reach the end of string string , print the permuation
        if i == len(s) - 1 :
            print(''.join(s))
        

        for j in range(i , len(s)) :
            # swap the curretn character with start character
            s[i] , s[j] = s[j] , s[i]
            backtrack(i + 1)
            # backtrack to swap characters back and try a new permutation
            s[i] , s[j] = s[j] , s[i]
    
    s = list(s)
    backtrack()


permuteString("ABC")
