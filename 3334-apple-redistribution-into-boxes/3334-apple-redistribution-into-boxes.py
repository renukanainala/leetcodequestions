class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        #apple.sort(reverse=True)

        k=0
        s=sum(apple)
        for i in range(len(capacity)):
            k+=capacity[i]
            if k>=s:
                return i+1
        return 0



