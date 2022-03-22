class Solution:
    
    
    hashMap = {}
    
    def climbStairs(self, n: int) -> int:
        
        if n in self.hashMap:
            return self.hashMap[n]
        
        if n==0: 
            return 1
        
        if n<0:
            return 0
        
        self.hashMap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.hashMap[n]
    
        