class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def longest_common_prefix(self):
        
        prefix = []

        node = self.root

        while node and not node.is_end_of_word and len(node.children) == 1:
            char,next_node = list(node.children.items())[0]
            prefix.append(char)
            node = next_node
        
        return ''.join(prefix)

def longest_common_prefix_helper(strings):
    if not strings:
        return ""

    trie = Trie()

    for string in strings:
        trie.insert(string)
    
    return trie.longest_common_prefix()

strings = ["flower" , "flow" , "flight"]
print("Longest common Prefix :" , longest_common_prefix_helper(strings))