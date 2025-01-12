class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        l = len(s)
        
        if l % 2 == 1:
            return False

        open = []
        unlocked = []

        for i in range(l):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                open.append(i)
            elif s[i] == ')':
                if open:
                    open.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open and unlocked and open[-1] < unlocked[-1]:
            open.pop()
            unlocked.pop()

        if not open and unlocked:
            return len(unlocked) % 2 == 0

        return not open