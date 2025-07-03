class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<=k:
            new=""
            for i in s:
                new=new+chr((ord(i)+1-ord('a'))%26+ord('a'))
            s=s+new
        return s[k-1]