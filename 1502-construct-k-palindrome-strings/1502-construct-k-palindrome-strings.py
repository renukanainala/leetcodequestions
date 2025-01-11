from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        c = Counter(s)
        c2= sum(f % 2 for f in c.values())
        return c2 <= k