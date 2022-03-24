class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)==1:
            return [strs]
        
        hashMap={}
        
        for i in range(len(strs)):
            
            x=list(strs[i])
            x.sort()
            
            if tuple(x) in hashMap:
                hashMap[tuple(x)].append(strs[i])
            else:
                hashMap[tuple(x)]=[strs[i]]
            
        return(hashMap.values())
            
            
        