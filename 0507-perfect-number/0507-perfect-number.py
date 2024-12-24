class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s=0
        for i in range(1,int(math.sqrt(num)+1)):
            if num%i==0:
                s+=i
                if num!=i*i:
                    s+=num/i
        return s==num+num