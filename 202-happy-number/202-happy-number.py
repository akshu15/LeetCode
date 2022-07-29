class Solution:
    def isHappy(self, n: int) -> bool:
        str1=str(n)
        total=n
        
        while total>4:
            total=0
            for i in range(len(str1)):
                el=str1[i]
                total+=int(el)**2
            str1=str(total)
            
            
        if(str1[0]=='1'):
            return True
        return 
            