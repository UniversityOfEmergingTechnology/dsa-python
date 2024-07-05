def insertion_sort(arr) :
    # i for current element
    # j will point to previous elements
    for i in range (1 , len(arr)):

        key = arr[i]
        j = i -1
        # b.c = O(n)
        # w.c and a.c = O(n^2)

        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key