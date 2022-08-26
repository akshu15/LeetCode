class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num ==0:
            return True
        
        string = str(num)
        
        string = string.rstrip('0')
        
        if num==int(string):
            return True
        return False
        
        