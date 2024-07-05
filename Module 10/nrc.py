from collections import deque

def firstNonRepeating(stream) :
    # hashmap to store character counts
    charCount = {}
    # queue to store characters
    q = deque()

    result = []

    for char in stream:
        # update char count
        charCount[char] = charCount.get(char , 0) + 1

        # add to queue if seeing for the first time
        if charCount[char] == 1:
            q.append(char)
        
        # remove chars from the front of the queue if they re repeating
        while q and charCount[q[0]] > 1:
            q.popleft()
        
        # the front of the queue is the first non repeating character
        result.append(q[0] if q else '#')

    return result

stream = 'aabccbd'
print(firstNonRepeating(stream))