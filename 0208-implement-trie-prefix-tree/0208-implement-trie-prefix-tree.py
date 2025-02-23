class Node:
    def __init__(self):
        self.child=[None]*26
        self.setend=False

class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        cur=self.root
        for i in word:
            ind=self.findindex(i)
            if not cur.child[ind]:
                cur.child[ind]=Node()
            cur=cur.child[ind]
        cur.setend=True   

    def search(self, word: str) -> bool:
        cur=self.root
        for i in word:
            ind=self.findindex(i)
            if not cur.child[ind]:
                return False
            cur=cur.child[ind]
        return cur.setend

    def startsWith(self, word: str) -> bool:
        cur=self.root
        for i in word:
            ind=self.findindex(i)
            if not cur.child[ind]:
                return False
            cur=cur.child[ind]
        return True
    def findindex(self,i):
        return ord('a')-ord(i)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)