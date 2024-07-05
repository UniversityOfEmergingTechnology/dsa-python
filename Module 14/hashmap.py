hashmap = {}

# insertion
hashmap["apple"] = 1
hashmap["banana"] = 2
hashmap["orange"] = 3

# lookup
print("Value for apple" , hashmap["apple"])

# deleting
del hashmap["banana"]

# updating
hashmap["orange"] = 5


print(hashmap)