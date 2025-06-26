class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -2  # special init so that if already sorted, end-start+1 = 0
        max_seen, min_seen = nums[0], nums[-1]

        for i in range(1, n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i

        for i in range(n - 2, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i

        return end - start + 1
