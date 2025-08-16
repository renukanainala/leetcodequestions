class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=[]
        k=num
        while k>0:
            ans.append(k%10)
            k=k//10
        ans1=0
        print(ans)
        f=True
        for i in ans[::-1]:
            if i==6 and f:
                ans1=ans1*10+9
                f=False
            else:
                ans1=ans1*10+i
        return ans1