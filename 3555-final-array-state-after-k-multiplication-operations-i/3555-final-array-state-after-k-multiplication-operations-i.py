import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        h=[(e,i) for i,e in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            e,ind=heapq.heappop(h)
            heapq.heappush(h,(e*m,ind))
        for e,ind in h:
            nums[ind]=e
        return nums