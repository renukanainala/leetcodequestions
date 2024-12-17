class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        s=[]
        area=0
        for i in range(len(h)):
            while s and h[s[-1]]>h[i]:
                ei=s.pop()
                pse=s[-1] if s else -1
                nse=i
                area=max(area,h[ei]*(nse-pse-1))
            s.append(i)
        while s:
            ei=s.pop()
            pse=s[-1] if s else -1
            nse=len(h)
            area=max(area,h[ei]*(nse-pse-1))
        return area