class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        span=1
        while self.s and self.s[-1][0]<=price:
            span+=self.s[-1][1]
            self.s.pop()
        self.s.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)