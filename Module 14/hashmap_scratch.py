class HashMap:

    def __init__(self,size = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self , key):
        # simple hash function

        # index lies in the range of 0 to size - 1
        return hash(key) % self.size
    

    def put(self,key , value):
        
        # insert a key value pair
        hash_index = self._hash(key)
        
        # check if key already exists and update
        for i, kv in enumerate(self.table[hash_index]):
            if kv[0] == key:
                self.table[hash_index][i] = (key , value)
                return
        # if key does not exist, append new key value pair
        self.table[hash_index].append((key,value))
    
    def get(self , key):
        # retrieve a value by key

        hash_index = self._hash(key)
        for kv in self.table[hash_index]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self , key):
        # remove a key value pair
        hash_index = self._hash(key)

        for i , kv in enumerate(self.table[hash_index]):
            if kv[0] == key:
                del self.table[hash_index][i]
                return
    


hashmap = HashMap()

hashmap.put("apple" , 1)
hashmap.put("banana",2)
hashmap.put("orange" , 3)

# print("Value for apple" ," ", hashmap.get("apple"))

hashmap.remove("banana")

hashmap.put("orange", 4)
# print("Updated value for orange" , " " , hashmap.get("orange"))

for i , bucket in enumerate(hashmap.table):
    if bucket:
        print(f"Bucket {i}: {bucket}")