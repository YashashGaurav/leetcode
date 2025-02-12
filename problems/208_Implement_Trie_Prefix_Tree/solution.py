"""
208. Implement Trie (Prefix Tree)
"""


class TrieNode:
    def __init__(self, children: dict = {}, eow_tag: bool = False):
        self.children = children
        self.EOW: bool = eow_tag


class Trie:
    def __init__(self):
        self.trie_root = TrieNode()

    def insert(self, word: str) -> None:
        current_node: TrieNode = self.trie_root

        for letter_index in range(len(word)):
            if word[letter_index] not in current_node.children:
                current_node.children[word[letter_index]] = TrieNode({})

            current_node = current_node.children[word[letter_index]]

            if letter_index == len(word) - 1:
                current_node.EOW = True

    def search(self, word: str) -> bool:
        current_node = self.trie_root
        for letter_index in range(len(word)):
            if word[letter_index] in current_node.children:
                current_node = current_node.children[word[letter_index]]
            else:
                return False

        return current_node.EOW

    def startsWith(self, prefix: str) -> bool:
        current_node = self.trie_root
        for letter_index in range(len(prefix)):
            if prefix[letter_index] in current_node.children:
                current_node = current_node.children[prefix[letter_index]]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
param_3 = obj.startsWith("a")
print(param_3)
