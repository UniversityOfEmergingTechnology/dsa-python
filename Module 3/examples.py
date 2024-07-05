import array

# append method

# intitalising an array of signed integers
arr = array.array('i' , [1,2,3])

print("Original array" , arr)

# appending a new element
arr.append(4)

print("Array after appending : " , arr)
print()

# inserting elements
print("Inserting elements using insert method ")
arr.insert( 2 , 5)
print("Array after inserting : " , arr)
print()

# pop method = removes and returns the element at the specified index

removed_element = arr.pop(2)
print("Array after popping : " , arr)
print()

# remove method = removes the first occurence of specified value
arr.append(1)
print("Appending one again " , arr)
arr.remove(1)
print()
print("After remove one" , arr)
print()


# index method = return the index of first occurence of specified value
print("Getting index of specified value : " , arr.index(4))

# reverse method will just reverse order of array elements

arr.reverse()
print(arr)


# typecode function - returns the data type with which array is initialized

print()
print("The datatype of array is " , arr.typecode)


# itemsize  - returns thwe size in bytes of a single array element

print("The itemsize of array " , arr.itemsize)


# buffer_info function - provides information about array's memory allocation

# memory address and number of elements

print()
print("The buffer info of array is " , arr.buffer_info())

# count() - find the number of occurences of a specific element in the array

arr.append(3)
arr.append(3)
arr.append(3)
print(arr)

print(arr.count(3))

# extend() - allows you to concatenate another array to the existing one

arr2 = array.array('i' , [1,2,3])
arr.extend(arr2)

print("The modified array " , arr )


# fromlist  - adds elements from a list to the end of array
li = [10,11,'apple']

arr.fromlist(li)

print()
print(arr)

# tolist converts an array to list

li2 = arr.tolist()

print()
print(li2)