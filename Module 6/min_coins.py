def minCoins(coins , target) :
    # base case if target amount is exactly 0 no more coins are needed
    if target == 0 :
        return 0
    
    # intitalise  result to a large value, we are looking for a minimum
    result = float("inf")

    # try every coin that has a value smaller than target amount

    for i in range(len(coins)) :
        if coins[i] <= target :
            sub_result = minCoins(coins , target - coins[i])

            # if sub_result is not infinity , update result

            if sub_result != float("inf") and sub_result + 1 < result :
                result = sub_result + 1
    
    return result

coins = [1,2,3]
target = 6

print(minCoins(coins , target))