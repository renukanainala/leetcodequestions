class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary1(l,h,arr): # searchoing for positive,negative
            ans=-1
            while l<=h:
                m=(l+(h-l)//2)
                if arr[m]<0:
                    ans=m
                    l=m+1
                else:
                    h=m-1
            return ans
        def binary(l,h,arr): # searchoing for positive,negative
            ans=len(arr)
            while l<=h:
                m=(l+(h-l)//2)
                if arr[m]>0:
                    ans=m
                    h=m-1
                else:
                    l=m+1
            return ans
        k=binary(0,len(nums)-1,nums) #first positive
        k1=binary1(0,len(nums)-1,nums) #last negative
        n=len(nums)
        print(1+k1,n-k)
        return max(len(nums)-k,1+k1)



        