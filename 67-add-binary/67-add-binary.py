class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #Binary to integer -> int(num,2)
        
        result=int(a,2)+int(b,2)
        
        #Integer to binary -> bin(num)[2:]
        
        return(bin(result)[2:])