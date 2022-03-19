class Solution:
    def romanToInt(self, s: str) -> int:
        
        s=list(s)
        # print(s)
        s.reverse()
        # print(s)
        
        
        hashMap={
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' :100,
            'D' : 500,
            'M' : 1000
        }
        if len(s)==1:
            return hashMap[s[0]]
        result = 0
        i=0
        
        while(i<len(s)-1):
            # print(i)
            curr=hashMap[s[i]]
            nex=hashMap[s[i+1]]
            # print('nex', nex)
            # print('curr',curr)
            
            if nex < curr:
    
                result+=(curr - nex)
                i+=2
            else:
                result+= (curr)
                i+=1
            
            if i==len(s)-1:
                result+=hashMap[s[len(s)-1]]    
                
            # print(result)
            
        # result+=hashMap[s[len(s)-1]]
                
        return(result)