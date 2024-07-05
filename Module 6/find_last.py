def find_last(s , char , index = None) :
    if index is None :
        index = len(s) - 1
    

    # base case if index is out of bounds character was not found
    if index < 0 : 
        return -1
    
    # if current character matches the target return the index
    if s[index] == char :
        return index
    

    return find_last(s , char , index - 1)

s = "hello world"
char = 'o'
print(find_last(s , char))