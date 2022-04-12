from collections import deque

class MyStack:

    def __init__(self):
        
        self.q = deque()
        
    def push(self, x: int) -> None:
        
        self.q.append(x)
        print(self.q)
        

    def pop(self) -> int:
        return(self.q.pop())

    def top(self) -> int:
        return(self.q[len(self.q)-1])

    def empty(self) -> bool:
        if(len(self.q))==0:
            return True
        else:
            return


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()