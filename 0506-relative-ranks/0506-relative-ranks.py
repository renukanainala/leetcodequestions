import heapq
class Solution:
    def findRelativeRanks(self,nums: List[int]) -> List[str]:
        h=[]
        for i in range(len(nums)):
            heapq.heappush(h,(-nums[i],i))
        r=[0]*len(nums)
        #print(h)
        for i in range(len(nums)):
            ele,ind=heapq.heappop(h)
            if i<3:
                if i==0:
                    r[ind]="Gold Medal"
                elif i==1:
                    r[ind]="Silver Medal"
                else:
                    r[ind]="Bronze Medal"
            else:
                r[ind]=str(i+1)
        return r

        