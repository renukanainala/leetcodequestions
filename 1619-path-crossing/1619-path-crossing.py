class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s=set()
        x,y=0,0
        s.add((0,0))    
        for i in path:
            if i=='N':
                y+=1
                
            elif i=='S':
                y-=1
            elif i=='W':
                x-=1
            else:
                x+=1
            if (x,y) in s:
                return True
            s.add((x,y))
        return False