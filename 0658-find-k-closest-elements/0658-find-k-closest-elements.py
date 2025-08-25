class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def findind(x):
            l=0
            h=len(arr)-1
            ans=len(arr)
            while l<=h:
                m=(l+h)//2
                if arr[m]>=x:
                    ans=m
                    h=m-1
                else:
                    l=m+1
            return ans
        ind=findind(x)
        print(ind)
        left=ind-1
        right=ind
        ans=[]
        n=len(arr)
        while left>=0 and right<n and k>0:
            if abs(x-arr[left])<=abs(x-arr[right]):
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
            k-=1
        while left>=0 and k>0 :
            ans.append(arr[left])
            left-=1
            k-=1
        while right<n and k>0:
            ans.append(arr[right])
            right+=1
            k-=1
        return sorted(ans)

