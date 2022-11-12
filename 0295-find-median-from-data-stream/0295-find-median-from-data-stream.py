import math
class MedianFinder:

    def __init__(self):
        self.stack = []
        

    def addNum(self, num: int) -> None:
        self.stack.append(num)

    def findMedian(self) -> float:
        self.stack.sort()
        length = len(self.stack)
        if length%2==0:      #Even
            # print(self.stack)
            a = math.floor((length-1)/2) 
            b = math.ceil((length-1)/2)
            # # print(length/2)
            # print(a, b)
            median = (self.stack[a]+self.stack[b])/2
            # print(median)
            return median
        else:
            # print("here",self.stack)
            # print(self.stack[length//2])
            return self.stack[length//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()