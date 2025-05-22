class Solution:
    def issafe(self,row,col,board,n):
        duprow=row
        dupcol=col
        for i in range(col):
            if board[row][i]=='Q':
                return False
        for i in range(row):
            if board[i][col]=='Q':
                return False
        
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1
        return True
    def create(self,col,board,n,ans):
        if col==n:
            ans.append(["".join(r) for r in board])
            return
        for row in range(n):
            if self.issafe(row,col,board,n):
                board[row][col]='Q'
                self.create(col+1,board,n,ans)
                board[row][col]="."
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        ans=[]
        self.create(0,board,n,ans)
        return ans
    