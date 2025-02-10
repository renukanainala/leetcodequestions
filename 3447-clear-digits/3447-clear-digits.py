class Solution:
    def clearDigits(self, s: str) -> str:
        x=[]
        for i in s:
            if x and i.isdigit():
                x.pop()
            else:
                x.append(i)
        return "".join(x)
    