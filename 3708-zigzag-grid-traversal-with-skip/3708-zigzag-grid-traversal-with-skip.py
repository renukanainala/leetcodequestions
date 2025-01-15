class Solution:
    def zigzagTraversal(self, g: List[List[int]]) -> List[int]:
        flag=True;ans=[]
        for i in range(len(g)):
            if i%2==0:
                for j in range(len(g[0])):
                    if flag:
                        ans.append(g[i][j])
                    flag=not flag
            else:
                for j in range(len(g[0])-1,-1,-1):
                    if flag:
                        ans.append(g[i][j])
                    flag=not flag
        return ans