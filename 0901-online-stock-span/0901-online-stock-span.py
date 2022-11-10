class StockSpanner:

    def __init__(self):
        self.output = []  # [[price, count]]

    def next(self, price: int) -> int:
        
        count = 1
        
        while self.output and self.output[-1][0]<=price:
            
            count+= self.output.pop()[1]
        
        self.output.append([price, count])
        return count
            
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)