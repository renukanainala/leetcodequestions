class MyCircularQueue:

    def __init__(self, k: int):
        self.cir=[0]*k
        self.front=-1
        self.rear=-1
        self.size=k
    def enQueue(self, value: int) -> bool:
        if self.isFull():  # Check if the queue is full
            return False
        if self.isEmpty():  
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.cir[self.rear] = value
        return True
    def deQueue(self) -> bool:
        if self.front==-1:
            return False
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return True

    def Front(self) -> int:
        if self.front==-1:
            return -1
        return self.cir[self.front]

    def Rear(self) -> int:
        if self.front==-1:
            return -1
        return self.cir[self.rear]


    def isEmpty(self) -> bool:
        return self.front==-1 

    def isFull(self) -> bool:
        return  (self.rear+1)%self.size==self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()