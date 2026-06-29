
# 208. Implement Trie (Prefix Tree)
class TrieNode(object):

    def __init__(self):
        self.children = {} #dict
        self.isWord = False


class Trie(object):

    def __init__(self):  
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for ch in word:
            if ch not in cur.children: # Create node if missing
                cur.children[ch] = TrieNode() 
            cur = cur.children[ch] # move to that node
        cur.isWord = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for ch in word:
            if ch not in cur.children: # check whether the ch exists as a key in dict
                return False
            
            cur = cur.children[ch]
        return cur.isWord 
            # check isWord bcz eg we can search app but only apple is inserted
    

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        # Suppose Trie contains apple and prefix=app, walk app -> success -> True
        cur = self.root

        for ch in prefix:
            if ch not in cur.children: return False
            cur = cur.children[ch]
        return True

# 1268. Search Suggestions System
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        root = TrieNode()
        products.sort()

        # Build Trie
        for word in products:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            if len(cur.suggestions) < 3: cur.suggestions.append(word)

        # Query
        cur = root
        res = []

        for char in searchWord:
            if cur and char in cur.children: 
                cur = cur.children[char]
                res.append(cur.suggestions)
            else:
                cur = None
                res.append([])

        return res









