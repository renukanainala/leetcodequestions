class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h={};c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=nums[i]*nums[j]
                if k not in h:
                    h[k]=[(nums[i],nums[j])]
                else:
                    h[k].append((nums[i],nums[j]))
                   # h[k].append(nums[j])
        #print(h)
    
        for i,j in h.items():
           # print(j)
            k=len(j) 
            if k>1:
                k1=(k*(k-1))//2 #no of two pairs picked from all pairs
                c+=k1*8 # for each pair 8 arrangements
        return c