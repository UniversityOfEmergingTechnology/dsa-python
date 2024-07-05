# define trienode class
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False
    

# define the trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self , word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    
    def search(self , word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word

    def starts_with(self , prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


trie = Trie()

trie.insert("apple")

print("Search 'apple' " , trie.search("apple"))
print("Search 'app' " , trie.search("app"))
print("Search 'app' " , trie.starts_with("app"))

trie.insert("app")
print("Search 'app' " , trie.search("app"))