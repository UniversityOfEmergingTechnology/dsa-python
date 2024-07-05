def removeAllOccurences(s , part) :
    # base case if part is not found in s return s
    if part not in s :
        return s
    

    # find index of first occurence of part in s and remove it
    new_s = s.replace(part , "" , 1)

    # recursive call with the updated string
    return removeAllOccurences(new_s , part)



s = "axxxyyyy"
print(removeAllOccurences(s , "xy"))