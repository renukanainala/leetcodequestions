class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums
        if a+b<=c or b+c<=a or c+a<=b:
            return "none"
        if a==b==c:
            return "equilateral"
        if a==b or b==c or c==a:
            return "isosceles"
        return "scalene"