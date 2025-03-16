class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        c=0
        for i in range(0,len(colors)):
            if colors[i%n]!=colors[(i+1)%n] and colors[(i+1)%n]!=colors[(i+2)%n]:
                c+=1
        return c
