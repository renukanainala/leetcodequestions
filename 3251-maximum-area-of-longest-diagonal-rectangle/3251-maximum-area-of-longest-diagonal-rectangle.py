class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mxcur=0;mxarea=0
        for u,v in dimensions:
            cur=u*u+v*v
            if cur>mxcur or (cur==mxcur and u*v>mxarea):
                    mxcur=cur
                    mxarea=u*v
        return mxarea