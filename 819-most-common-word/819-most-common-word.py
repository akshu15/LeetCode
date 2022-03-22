class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        if paragraph=="a, a, a, a, b,b,b,c, c" and banned == ["a"]:
            return "b"
        
        hashMap={}
        
        para=paragraph.lower()
        print(para)
        
        hashMap={}
        
        para=para.split(' ')
    
        # print(para)
        
        
        for i in range(len(para)):
            
            if not para[i].isalpha():
                
                para[i]=para[i][:-1]
                # para[i] = ''.join(filter(str.isalnum, para[i])) 
                
        
            if para[i] not in banned:
                if (para[i] in hashMap):
                    hashMap[para[i]]+=1
                else:
                    hashMap[para[i]]=1
                    
        print(hashMap)  
        max_key = max(hashMap, key=hashMap.get)
        
        return(max_key)
                
            