# define the trieNode class

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


# define the trie class

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self , word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True


    def search_prefix(self , prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    def collect_all_words(self , node , prefix, words):
        # base case
        if node.is_end_of_word:
            words.append(prefix)
        
        for char,next_node in node.children.items():
            self.collect_all_words(next_node , prefix + char ,words)
    
    def autocomplete(self , prefix):
        # get last node of the prefix
        node = self.search_prefix(prefix)

        if not node :
            return []

        words = []
        # build all words from the prefix
        self.collect_all_words(node , prefix , words)
        return words

trie = Trie()
words = ["flower" , "flock" , "flour" , "fluke" , "flight" , "mudit" , "apple" , "ball"]

for word in words:
    trie.insert(word)

prefix = "m"

print("Autocomplete suggestions for '{}':".format(prefix),trie.autocomplete(prefix))