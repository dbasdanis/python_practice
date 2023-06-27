class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def print_trie(self):
        self._print_trie_recursive(self.root, "")

    def _print_trie_recursive(self, node: TrieNode, indent: str):
        if node.is_end_of_word:
            print(indent + "- (end)")
        for char, child in node.children.items():
            print(indent + "- " + char)
            self._print_trie_recursive(child, indent + "  ")