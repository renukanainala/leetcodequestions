class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s=set()
        q=deque()
        q.append(0)
        s.add(0)
        while q:
            n=q.popleft()
            for i in rooms[n]:
                if i not in s:
                    q.append(i)
                    s.add(i)
        return len(s)==len(rooms)