class Solution:
    def isHappy(self, n: int) -> bool:
        str1=str(n)
        total=n
        
        while total>4:
            total=0
            for i in range(len(str1)):
                # print(str1[i])
                el=str1[i]
                total+=int(el)**2
            str1=str(total)
            
        # if total<4:
            
        if(str1[0]=='1'):
            return True
        return 
            