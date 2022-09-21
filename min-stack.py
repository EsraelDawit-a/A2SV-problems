class MinStack:

    def __init__(self):
        self.stac = []
        

    def push(self, val: int) -> None:
        self.stac.append(val)
        

    def pop(self) -> None:
        self.stac.pop()
        

    def top(self) -> int:
        return self.stac[-1]
        

    def getMin(self) -> int:
        return min(self.stac)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()