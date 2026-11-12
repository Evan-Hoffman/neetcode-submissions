class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = True
        

    def search(self, word: str) -> bool:

        def dfs(node, word) -> bool:
            curr = node

            for i, c in enumerate(word):
                if c == '.':
                    found = False
                    for child in curr.children.values():
                        if dfs(child, word[i + 1:]):
                            found = True
                    
                    return found
                
                elif c not in curr.children:
                    return False

                curr = curr.children[c]
            
            return curr.word

        return dfs(self.root, word)

        


        
